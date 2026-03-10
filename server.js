const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient } = require('mongodb'); // 修正了这里的导入语法
const path = require('path');

const app = express();
const port = 3000;

// 1. 解析 JSON 和 URL 编码数据
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// 2. 静态文件服务 (指向你存放 index.html 的 public 文件夹)
app.use(express.static(path.join(__dirname, 'public')));

// 3. MongoDB 连接配置
// 账号: admin, 密码: password, 地址: localhost (因为 Node 在宿主机，Docker 映射了 27017)
// 优先使用环境变量中的地址，如果没有则默认使用 localhost（方便本地开发调试）
const url = process.env.MONGO_URL || 'mongodb://admin:password@localhost:27017';
const client = new MongoClient(url);
const dbName = 'user-account'; 

async function main() {
    try {
        // 连接数据库
        await client.connect();
        console.log('Successfully connected to MongoDB container! ✅');
        
        const db = client.db(dbName);
        const collection = db.collection('users');

        // API: 获取用户数据
        app.get('/get-profile', async (req, res) => {
            try {
                // 查找 userid 为 1 的用户
                const user = await collection.findOne({ userid: 1 });
                // 如果找不到，返回默认空对象
                res.send(user ? user : { name: '', email: '', interests: '' });
            } catch (err) {
                console.error("Error fetching profile:", err);
                res.status(500).send("Error fetching profile");
            }
        });

        // API: 更新用户数据
        app.post('/update-profile', async (req, res) => {
            try {
                const userObj = req.body;
                console.log("Saving data:", userObj);
                
                userObj['userid'] = 1; // 强制 ID 为 1
                
                // upsert: true 表示如果不存在则创建一个新的
                await collection.updateOne(
                    { userid: 1 }, 
                    { $set: userObj }, 
                    { upsert: true }
                );
                
                res.send(userObj);
            } catch (err) {
                console.error("Error updating profile:", err);
                res.status(500).send("Error updating profile");
            }
        });

        // 4. 启动 Express 服务器
        app.listen(port, () => {
            console.log(`Node app listening on port ${port}`);
            console.log(`Access the app at http://localhost:${port}`);
        });

    } catch (error) {
        console.error('Failed to connect to MongoDB:', error);
        process.exit(1); // 连接失败则退出程序
    }
}

// 运行主函数
main();