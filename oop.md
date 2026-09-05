override means
parents has the base main functions then child class take the method from the parents class and override the parents main methods and use child class own method

clear explanation from chatgpt: The parent class has a method. The child class inherits that method, but the child can override it by providing its own implementation of that same method.

Class = 模板

Object = 根据模板制造出来的东西


Student s1 = new Student();
Student s2 = new Student();

Student class
      ↓
   ┌──┴──┐
   ↓     ↓
  s1     s2

—————————————
**example
class Animal {
    void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

——————

void = Am I going to use the answer from this method somewhere else?

————————

OOP
↓
用 Class + Object 来组织程序

Interface
↓
规定“你必须提供什么功能”

List
↓
存放一堆 Object

Exception
↓
处理程序发生的问题

—————————————

List<Student> students;

脑中可以直接翻译成：

“一个叫 students 的 List，准备拿来装 Student 对象。”

—————————————

Machine m1 = new Machine();

Machine       → Class / type
m1            → reference variable
new Machine() → Object

——————————————
extends
↓
“我是你的孩子，我继承你的东西”

implements
↓
“我遵守你的规则，我保证有这些功能”

|     | Inheritance        | Interface             |
| --- | ------------------ | --------------------- |
| 关键词 | `extends`          | `implements`          |
| 意思  | 继承别人               | 遵守规则                  |
| 例子  | Dog extends Animal | Dog implements Animal |
| 重点  | **拿到父 Class 的东西**  | **必须提供规定的功能**         |
