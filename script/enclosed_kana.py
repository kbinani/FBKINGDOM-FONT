a = Array(94)
i = 0
while (i < 94)
  a[i] = 0
  i++
endloop

from = 0u3042 #あ
to = 0u32d0 #㋐
i = 0
while (from <= 0u304a) #お
  a[i++] = to
  a[i++] = from
  from += 2
  to++
endloop

from = 0u304b #か
to = 0u32d5 #㋕
while (from <=0u3061) #ち
  a[i++] = to
  a[i++] = from
  from += 2
  to++
endloop

from = 0u3064 #つ
to = 0u32e1 #㋡
while (from <=0u3068) #と
  a[i++] = to
  a[i++] = from
  from += 2
  to++
endloop

from = 0u306a #な
to = 0u32e4 #㋤
while (from <=0u306e) #の
  a[i++] = to
  a[i++] = from
  from++
  to++
endloop

from = 0u306f #は
to = 0u32e9 #㋩
while (from <=0u307b) #ほ
  a[i++] = to
  a[i++] = from
  from += 3
  to++
endloop

from = 0u307e #ま
to = 0u32ee #㋮
while (from <=0u3082) #も
  a[i++] = to
  a[i++] = from
  from++
  to++
endloop

from = 0u3084 #や
to = 0u32f3 #㋳
while (from <=0u3088) #よ
  a[i++] = to
  a[i++] = from
  from += 2
  to++
endloop

from = 0u3089 #ら
to = 0u32f6 #㋶
while (from <=0u308d) #ろ
  a[i++] = to
  a[i++] = from
  from++
  to++
endloop

i = 0
while (i < 94)
	to=a[i]
	from=a[i + 1]
	if (from == 0 || to == 0)
		break
	endif
	SelectNone()
	Select(from)
	Copy()
	SelectNone()
	Select(to)
	Clear()
	Paste()
	SetWidth(1000)
	CenterInWidth()
	Scale(65)
	Import("../glyph/enclosure.svg")
	SetWidth(1000)
	AutoHint()
	i = i + 2
endloop
