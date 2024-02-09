# 클래스 정의
class Xlsx_Read:
    # 생성자 메서드 (인스턴스를 생성할 때 호출됨)
    def __init__(self, filename, ):
        # 인스턴스 변수 초기화
        self.x = x
        self.y = y
    
    # 메서드 정의
    def add(self):
        return self.x + self.y
    
    def multiply(self):
        return self.x * self.y

# 클래스를 이용하여 객체(인스턴스) 생성
obj1 = MyClass(5, 3)
obj2 = MyClass(10, 2)

# 객체의 속성에 접근
print(obj1.x)  # 출력: 5
print(obj2.y)  # 출력: 2

# 객체의 메서드 호출
print(obj1.add())  # 출력: 8
print(obj2.multiply())  # 출력: 20

# 클래스 변수에 접근
print(MyClass.class_variable)  # 출력: 10
