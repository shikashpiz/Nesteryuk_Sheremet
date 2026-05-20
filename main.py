import ifcopenshell
import ifcopenshell.api
import ifcopenshell.util.element


IFC_FILEPATH = "Example_1.ifc"
MIN_WIDTH = 0.8
MODIFIED_OUTPUT = "modified_variant.ifc"
FILTERED_DOORS_OUTPUT = "doors_filtered_output.ifc"


class IfcModelAnalyzer:
    def __init__(self):
        self.model = None
        self.walls = []
        self.first_wall = None
        self.narrow_doors = []

    def load(self):
        # Загружаю модель один раз, дальше методы работают с self.model.
        self.model = ifcopenshell.open(IFC_FILEPATH)

    def count_walls(self):
        print("===== Задание 1. Количество стен =====")
        self.walls = self.model.by_type("IfcWall")
        print("Стен найдено:", len(self.walls))

    def show_first_wall(self):
        print("\n===== Задание 2. Первая стена =====")
        if len(self.walls) > 0:
            self.first_wall = self.walls[0]
            print("GlobalId:", getattr(self.first_wall, "GlobalId", None))
            print("Name:", getattr(self.first_wall, "Name", None))
            print("ObjectType:", getattr(self.first_wall, "ObjectType", None))
            print("IFC-тип:", self.first_wall.is_a())
        else:
            print("Стен нет.")

    def show_first_wall_psets(self):
        print("\n===== Задание 3. Property Sets первой стены =====")
        if self.first_wall is None:
            print("Нет первой стены для вывода Pset.")
            return
        psets = ifcopenshell.util.element.get_psets(self.first_wall)
        if not psets:
            print("Pset пустые.")
        for pset_name, props in psets.items():
            print("Pset:", pset_name)
            for prop_name, prop_value in props.items():
                print(" ", prop_name, "=", prop_value)

    def show_storeys(self):
        print("\n===== Задание 4. Этажи и схема модели =====")
        storeys = self.model.by_type("IfcBuildingStorey")
        print("Схема файла:", self.model.schema)
        print("Количество этажей:", len(storeys))
        if len(storeys) == 0:
            print("Этажи не найдены.")
        for st in storeys:
            print("Этаж:", getattr(st, "Name", None), "Elevation:", getattr(st, "Elevation", None))

    def find_narrow_doors(self):
        print("\n===== Задание 5. Двери =====")
        doors = self.model.by_type("IfcDoor")
        if len(doors) == 0:
            print("Дверей нет.")
        for door in doors:
            w = getattr(door, "OverallWidth", None)
            h = getattr(door, "OverallHeight", None)
            print("Дверь:", getattr(door, "Name", None), "ширина:", w, "высота:", h)
            if w is not None and w < MIN_WIDTH:
                self.narrow_doors.append(door)

        print("\n===== Задание 6. Узкие двери =====")
        for door in self.narrow_doors:
            print("Узкая дверь:", getattr(door, "Name", None), "ширина:", getattr(door, "OverallWidth", None))
        print("Всего:", len(self.narrow_doors))

    def modify_wall(self):
        print("\n===== Задание 7. Изменение стены =====")
        if self.first_wall is None:
            print("Первой стены нет, изменение не выполняется.")
        else:
            name = getattr(self.first_wall, "Name", None)
            if name is None:
                name = "Без имени"
            self.first_wall.Name = "MODIFIED_" + name

            # В IFC свойства могут быть уже созданы, поэтому сначала проверяю старые связи.
            pset = None
            for rel in getattr(self.first_wall, "IsDefinedBy", []) or []:
                definition = getattr(rel, "RelatingPropertyDefinition", None)
                if definition is not None and definition.is_a("IfcPropertySet"):
                    if getattr(definition, "Name", None) == "Pset_WallCommon":
                        pset = definition
            if pset is None:
                pset = ifcopenshell.api.run("pset.add_pset", self.model, product=self.first_wall, name="Pset_WallCommon")
            ifcopenshell.api.run("pset.edit_pset", self.model, pset=pset, properties={"IsExternal": True})
            print("Стена изменена.")

        self.model.write(MODIFIED_OUTPUT)
        print("Сохранено:", MODIFIED_OUTPUT)

    def export_filtered_doors(self):
        print("\n===== Задание 7. Экспорт отфильтрованных дверей =====")
        try:
            file2 = ifcopenshell.file(schema=self.model.schema)
            for typ in ["IfcProject", "IfcSite", "IfcBuilding", "IfcBuildingStorey"]:
                for x in self.model.by_type(typ):
                    file2.add(x)
            for door in self.narrow_doors:
                file2.add(door)
            file2.write(FILTERED_DOORS_OUTPUT)
        except Exception as error:
            # Если библиотека не дает скопировать объекты отдельно, делаю обычную копию модели.
            print("Ошибка экспорта:", error)
            self.model.write(FILTERED_DOORS_OUTPUT)

        check = ifcopenshell.open(FILTERED_DOORS_OUTPUT)
        print("Файл сохранен:", FILTERED_DOORS_OUTPUT)
        print("Дверей после открытия:", len(check.by_type("IfcDoor")))

    def run(self):
        try:
            self.load()
        except Exception as error:
            print("Не удалось открыть IFC:", error)
            return
        self.count_walls()
        self.show_first_wall()
        self.show_first_wall_psets()
        self.show_storeys()
        self.find_narrow_doors()
        self.modify_wall()
        self.export_filtered_doors()


if __name__ == "__main__":
    a = IfcModelAnalyzer()
    a.run()
