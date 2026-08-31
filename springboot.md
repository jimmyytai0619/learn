前端
 ↓
Spring Boot
 ↓
Java代码
 ↓
Database
 ↓
Spring Boot
 ↓
前端

——————

Spring Boot 里面最重要的 4 个东西

1. Controller 负责接收请求。

@RestController
public class StudentController {

    @GetMapping("/student")
    public String getStudent() {
        return "John";
    }
}

2. Service 负责做事情 / 处理逻辑。

@Service
public class StudentService {

    public String getStudent() {
        return "John";
    }
}

3. Repository 负责跟 Database 沟通。

4. Entity 代表数据库里面的数据。

@Entity
public class Student {

    private Long id;
    private String name;
    private int age;
    private String course;
}

结构 :
                User
                 ↓
            Controller
                 ↓
              Service
                 ↓
            Repository
                 ↓
             Database

Spring Boot 只是做网站和 API？

不是。

Spring Boot 最常见的用途确实是：

🌐 网站后端
🔌 REST API
📱 给手机 App 提供后端
🗄️ Database 系统
🏢 企业系统
⚙️ 后台服务
🔄 Microservices（微服务）
⏰ 定时任务、后台程序等

所以更准确地说：

Spring Boot 是一个用 Java 开发各种后端应用的 framework。