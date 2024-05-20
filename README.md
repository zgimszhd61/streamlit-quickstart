# streamlit-quickstart

要在阿里云ECS上部署Streamlit应用的快速入门指南，可以按照以下步骤进行：

### 准备工作

1. **注册阿里云账号**：如果你还没有阿里云账号，需要先注册一个。
2. **创建ECS实例**：登录阿里云控制台，创建一个ECS实例。选择合适的操作系统，推荐使用Ubuntu 18.04或更高版本。
3. **配置安全组**：确保ECS实例的安全组规则中开放了Streamlit默认使用的8501端口，以便外部访问。

### 安装环境

1. **连接到ECS实例**：使用SSH连接到你的ECS实例。
2. **安装Python**：确保Python3已安装。你可以使用`python3 --version`来检查Python版本。
3. **安装pip**：如果还没有安装pip，可以使用`sudo apt-get install python3-pip`来安装。
4. **安装Streamlit**：通过pip安装Streamlit，命令为`pip3 install streamlit`。

### 创建Streamlit应用

1. **创建一个新的Python脚本**：在ECS实例上创建一个新的Python脚本，例如`app.py`。
2. **编写Streamlit应用**：在`app.py`中编写你的Streamlit应用代码。以下是一个简单的示例：

```python
import streamlit as st

st.title('Hello Streamlit')
st.write('This is a quickstart Streamlit app deployed on Aliyun ECS.')
```

### 运行Streamlit应用

1. **启动应用**：在ECS实例的命令行中，运行`streamlit run app.py`来启动你的Streamlit应用。
2. **访问应用**：在浏览器中访问`http://<ECS实例的IP地址>:8501`，你应该能看到你的Streamlit应用正在运行。
3. **80端口应用**：如果想要80端口，对应命令为`sudo streamlit run app.py --server.port 80`来启动你的Streamlit应用。

### 注意事项

- 确保你的ECS实例的公网IP地址是可以访问的，并且8501端口没有被防火墙或安全组规则阻止。
- 根据你的应用需求，可能还需要安装额外的Python库或进行其他配置。

以上步骤提供了在阿里云ECS上部署Streamlit应用的基本指南。根据具体的应用需求和环境配置，可能还需要进行一些额外的设置或调整。

Citations:
[1] https://mirror.baidu.com/pypi/simple/
[2] https://github.com/mycaule/reading-resources
[3] https://github.com/roblaszczak/awesome-go-1
[4] https://zenodo.org/records/6854770/files/repo_list.txt?download=1
[5] https://www.oschina.net/informat/%E4%BF%9D%E5%AD%98%E5%BE%AE%E8%B0%83%E5%90%8E%E7%9A%84%E6%A8%A1%E5%9E%8B%20huggingface
[6] https://developer.aliyun.com/note/257557996
[7] https://developer.aliyun.com/article/57532
[8] https://repo.huaweicloud.com/repository/pypi/simple/
