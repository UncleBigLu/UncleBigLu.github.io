# CSS

## selector

| selector | function                                                   |
| -------- | ---------------------------------------------------------- |
| *        | Universal selector(\*)selects all HTML elements on the page |
| element Selector(eg: p{}) | Select based on the element name |



### margin

给元素设定外边距属性，定义元素周围的空间。可接收1-4个值。

#### 可取值

- length 以固定值为外边距
- percentage 相对于包含块的宽度，以百分比值为外边距
- Auto 浏览器自动决定。

### padding

控制元素内边距。

#### 可取值

- length
- percentage

![VlwVi](https://www.runoob.com/wp-content/uploads/2013/08/VlwVi.png)



### background

一种css简写属性，用于一次性集中定义各种背景属性，包括 color, image, origin 与 size, repeat 方式等等。

```css
/* 使用 <background-color> */
background: green;

/* 使用 <bg-image> 和 <repeat-style> */
background: url("test.jpg") repeat-y;

/* 使用 <box> 和 <background-color> */
background: border-box red;

/* 将背景设为一张居中放大的图片 */
background: no-repeat center/80% url("../img/image.png");
```



### min-height:

元素最小高度，防止height属性的应用值小于min-height

### position

定义建立元素布局的定位机制。

| value    | description                                                  |
| -------- | ------------------------------------------------------------ |
| absolute | 生成绝对定位的元素，相对于 static 定位以外的第一个父元素进行定位。元素的位置通过 "left", "top", "right" 以及 "bottom" 属性进行规定。 |
| fixed | 绝对定位，相对浏览器窗口定位 |
| relative | 相对定位， 相对于其正常位置进行定位。|
| static | 默认值，无定位 |
| inherit | 从父元素继承position |

#### relative相对定位完成的过程：

- 首先按默认方式（**static**）生成一个元素(并且元素像层一样浮动了起来)。
- 然后相对于以前的位置移动，移动的方向和幅度由 **left**、**right**、**top**、**bottom** 属性确定，偏移前的位置保留不动。



### overflow

定义溢出元素内容区的内容如何处理。

| value    | description                                                  |
| -------- | ------------------------------------------------------------ |
| Visible | 默认值。元素不会被修剪，会呈现在元素框外 |
| Hidden | 内容会被修剪，溢出内容不可见 |
| Scroll | 内容会被修剪，提供滚动条查看剩余内容 |
| auto | 若内容被修剪，则提供滚动条查看 |
| inherit | 从父元素继承overflow |

### object-fill

定义replaced element如何resize来fit container。

详见[此文](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)



### before

**`::before`** 创建一个[伪元素](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements)，其将成为匹配选中的元素的第一个子元素。常通过 [`content`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/content) 属性来为一个元素添加修饰性的内容。此元素默认为行内元素。

Eg: Insert some text before the content of each <p\> element:

```css
p::before{
  content:"Read this"
}
```

### after

同理，其将成为匹配选中的元素的最后一个子元素

### linear-gradient()

用于渐变色。详见[此文](https://developer.mozilla.org/en-US/docs/Web/CSS/linear-gradient())

### mix-blend-mode

混合模式
