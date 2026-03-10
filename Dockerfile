FROM node:20-alpine

# 1. 设置工作目录（一定要有）
WORKDIR /home/app

# 2. 先把 package.json 拷进去安装依赖（利用缓存）
COPY package*.json ./
RUN npm install

# 3. 再把所有代码（包括 server.js）拷进去
COPY . /home/app/

# 4. 启动命令
CMD ["node", "server.js"]