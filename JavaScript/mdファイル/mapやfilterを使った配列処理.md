## map&filter を使って配列を処理する

```
const nameArr = ['田中','山田','野田'];
```

従来の方法

```
for (let index = 0; index < nameArr; index++){
    console.log(nameArr[index]);
}
```

結果

```
田中
山田
野田
```

map を使って同じ処理をする

```
const nameArr2 = nameArr.map((name) => {
    return name;
    cosole.log(nameArr2);
})
```

or

```
nameArr.map((name) => console.log(name));
```

結果

```
['田中','山田','野田']
```

filter を使って処理をする

```
const numArr = [1,2,3,4,5];
ある条件に一致するものだけ出力
const newNumArr = numArr.filter((num) =>{
    return num % 2 === 1;
)};
cosnole.log(newNumArr);
```

結果

```
[1,3,5]
```

テンプレート文字列を使う

```
const nameArr = ['田中','山田','野田'];

for (let index = 0; index < nameArr; index++){
    console.log('${index + 1}番目は${nameArr[index]}です');
}
```

結果

```
一番目は田中です
二番目は山田です...
```

map で処理するには

```
nameArr.map((name,index) => console.log('${index + 1}番目は${name}です'));
```
