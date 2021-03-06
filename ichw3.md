# 作业3

## 高速缓冲存储器

缓存（Cache）直观而言，就相当于我们每天喝水用水壶。 电脑存储空间相当于宿舍外面的热水处，而缓存相当于我们手里的水壶，我们则相当于CPU。
有了水壶，我们不用天天长途跋涉到宿舍公用热水处饮水，只要一次性灌满水壶就能喝，从而大大提高了效率。

**Cache的结构**

我们知道，内存的结构包含地址和地址内存储的信息，而缓存则是调用内存的信息。所以Cache首先要包含所调用内存中的数据（data），还要包括数据对应的地址信息（tag）。为了增加寻找信息的速度，Cache外加“有效位（valid）”，用以判断这行信息是否能够被有效使用。

在数据从内存映射到cache时，根据物理地址的中间三位（index字段）来定位当前数据应该在cache的哪一行，把物理地址的前两位(tag字段)和该地址对应的内容放入对应的cache line（缓存的每一行）的tag字段和data字段。那么在之后进行cache寻找的时候就可以根据cache line的tag字段来辨认当前line中的数据是数据哪个数据块的。

**Cache的工作原理**

CPU读取数据的顺序是先缓存后内存。

如果Cache中有数据，那么直接调过来读就行了。

如果Cache中缺少要用的数据，那么就用相对慢的速度从内存中读取并送给CPU处理，同时把这个数据所在的数据块调入Cache中，可以使得以后对整块数据的读取都从Cache中进行，不必再调用内存。

一般来讲，CPU能读取缓存中数据占大部分，即我们只需调用一小部分内存里的数据即可。而为了增大运行速度，我们可以再增加一级Cache，那么CPU一次所调用数据会有更大的部分来自Cache，那么运行速率会显著上升。
