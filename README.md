## 划时代的家用智能信息服务系统
![](http://box.hayoou.com/1587545534464/640.webp)  
来了！

Mini 智库 ，比手掌还小的家居设备（已拆外壳）

产品图文介绍：[http://hayoou.com/minizk](http://hayoou.com/minizk)

* 帮助你解决日常信息收集，个人信息整理

* 智能化信息推荐，全新的第三方生态开放平台

尽在 Mini 智库！！

我们的第一个解决方案就是：

帮你阅读微信朋友圈！！

* 如果你加了几千人相关领域的朋友，

* 如果你没有时间看朋友圈

那么 在你睡觉的时候，这个机器将自动整理你朋友圈的关键词和新出来的行业动向

只需要连接 USB 到Mini智库即可

现已在淘宝体验价发售：
[https://item.taobao.com/item.htm?id=616564017531](https://item.taobao.com/item.htm?id=616564017531)

处理结果，使用权重排序算法，剔除无效关键词

采用人工智能的OCR算法和分词统计算法

所有信息存储在本地，所有软件更新由我们掌控，

我们会对新添加的软件代码进行逐一审核。

开放的软件平台和第三方开源软件，让你掌控自己的数据中心

Mini智库已经编译和安装 :

- [x]  pytorch 1.20a + torchvision 0.50
- [x]  Tensorflow 1.14
- [x]  Opencv
等AI基础开发框架。

还安装了Golang1.14 Php nginx python3.7.7 xrdp gnome(远程桌面）,自动CPU频率控制，mini智库远程自动更新，ffmpeg ,glibc ,等基础软件

AI 相关软件示例：

[https://github.com/youkpan/YOLOv3_TensorFlow](https://github.com/youkpan/YOLOv3_TensorFlow)

使用tensorflow 框架用YOLOv3 模型进行目标检测识别。

[https://github.com/youkpan/pytorch-yolo-v3](https://github.com/youkpan/pytorch-yolo-v3)

使用pytorch框架用YOLOv3 模型进行目标检测识别。

[https://github.com/youkpan/Yet-Another-EfficientDet-Pytorch](https://github.com/youkpan/Yet-Another-EfficientDet-Pytorch)

使用pytorch框架用efficient模型进行目标检测识别。
 

产品内容：

* Orangepi 4 开发板
* 外壳加散热片及风扇
* USB 转串口
* SD 卡 64GB ，已写好程序
* 说明文档

产品文档下载：[http://hayoou.com/minizk](http://hayoou.com/minizk)

第三方软件开发商对接说明：
1、用户帐户 存储在 /data/apps/hayoou/userinfo.txt 中。其中 user 信息可用于唯一用户凭证。

2、在发布平台： zk.hayoou.com 提交你的软件 ，经过审核后，可发布到所有mini智库机器中。建议将代码放置在 github中，我们会安排时间人工审核。

3、软件更新、发布 人工通道： 微信 hayoou2 ，Email:hayoou_com@126.com

4、用户存储空间标准为 128GB ，请注意软件发布的大小。通常在1GB之内。

5、禁止将用户个人信息远程存储、暴露后台权限 等危害用户信息安全的行为和手段，即使是非主观，一经查出根据我们的规则和处理，冻结发布账号和发布黑名单。

6、树莓派相关生态都比较成熟，在全球已经售出2800万套开发板。未来家用服务市场广阔，我们希望能和你们一起完善mini智库相关软件，更好的为用户提供个人信息数据服务。

##如何训练一个面向未来的通用智能体

我们（哈友社区）在不断探索科技与应用相结合，做了很多项目，也带来了思考。

如何让更有创造能力的智慧体辅助我们的工作。

现在越来越多专业的机器人进入了各个角色，造车，电子等等，但是在人类的一些日常生活中却经常存在一些通用的需求没有得到满足。

我们都知道，手机里有一个助手，可以帮忙打电话，发消息，设置日程提醒等，但我们如果想在淘宝选一个产品，却没有这样的智能服务我们。哪怕我们愿意多等几个小时（睡前下任务，醒来可以看到结果）

几年前，我们有一个大想法，就是创造出一个具有准大学生的常识和行动能力的通用智能。这样，在各个行业和领域只需要进行专业化的训练即可完成通常的任务。但考虑到人脑的海量神经元数量和对比机器的功耗，我没有在这个领域深研下去。

最近有时间，又做了一些小项目，发现一些工作内容比较繁琐，于是想起了这个概念。

所以整理了一下相关的需求和目标，探讨下，这类机器的可实现程度。

目标：一系列可以独立运行，具有智能化学习和任务执行的软件工具。

* 阶段1：识别意图，接入网络搜索结果，根据个性化信息整理数据。如：找一张苹果的照片，不是苹果手机，是水果

* 阶段2：根据更详细的信息进行数据检索，如：在58同城帮我留意下附近的房源信息，我打算10天内换房子。价格在 1XXX到 3xxxx。位置。。。

* 阶段3：工作辅助，如自动整理文档，整理照片，挑选合适的内容存储和自动化通知发送，自动补全代码，分析数据差异，理解工作内容

* 阶段4：自动整理数据和安装其他软件。能够在公开的信息中，自动生成软件，或者根据 github等开源代码，为自己的系统增加功能。

* 阶段5：像人类一样从事创造力的工作：小说，剧本，代码，设计，思考，分析，投资，信息挖掘等。

当然上面这些有的只是临时的想法，毕竟还有十几亿印度人在找事做。在成本和时间上，很难面面俱到地去实现。很多科幻电视剧也有类似的剧本。有的时候人类的智慧成本很低（吃进去的是米饭，挤出来的是代码）。有的时候又很高。在很多地方确实能够用上重复的机器完成，并且有可以看见收益的场景，基本上已经有布局和产品了。

所以 ，我们只挑选一个小小的场景进行切入，就是个人服务方面的软件集合。当然欢迎大家对上面通用智能进行整理，我只是抛砖引玉。

目前来说，普通人对信息需求也可以说强烈，也可以说不强烈。但人们越来越认识到 个性化的信息更重要。相比今日头条来说，它覆盖的信息还是太广，或者不够精准具体，无法直接进入个人生活的方面，只是从比较大的场景和社会现象来影响普通人。我们希望这一系列智能化软件能够在工作和生活中直接有收益。

比如小米音箱 ，我们也知道，它有很多很多功能 比如背唐诗 设置闹钟等，但我们还不会想到去问它 美国现在有多少人确诊了，帮我搜索一个某某产品，价格 xx 到 yy 。并且支付。因为虽然是几句话，但是要根据个人信息综合判断。国外有买手 ，专门服务一些富豪，挑选一些重要的礼品。但这些信息整理工作却需要非常多的知识和线下的认知及反馈。有些，我们也承认，不可能由机器来完成

但是，如果一个非常懂你，理解个人需求的智慧体，是会在工作和生活上提高更多的效率。

我们前阵子花了很多时间选了一个小小的机器，也在这个机器上进行初步的开发工作，目前已经实现了语音识别等功能。我们希望未来能够跑哈友个性化方面的服务。

目前还没有外观方面的调整，其实这也是一种科技美（哈哈）

里面有 6个 核心，4GB DDR4 RAM ，16GB 存储，可以扩展256GB和移动硬盘 TB级别。

主要功能：

1、收集拥有者的所有信息 （存储在本地）

2、整理信息，推荐

3、自动更新自身软件

4、自定义开发，可通过第三方服务商定制服务。

未来可能会开发如下方向:

1、打通和微信的桥梁 参考我们之前的工作（朋友圈数据整理，智慧虚拟好友等）

2、识别图片文字，进行图片信息整理（通过了解相册了解拥有者的信息）

3、互联网数据收集，推荐。从互联网采集大量信息，筛选过滤对拥有者有用的信息。

4、智慧型助手，根据以上信息进行个性化提醒和对外沟通。

5、整理更多相关资源和架构方面的思考，提供给软件开发服务商，进行统一的框架设计，组织管理内部软件结构。

预计第一批售价在1600~ 3000，将于5月份发布。

预售联系微信 hayoou2

现已在淘宝体验价发售：
[https://item.taobao.com/item.htm?id=616564017531](https://item.taobao.com/item.htm?id=616564017531)

 
