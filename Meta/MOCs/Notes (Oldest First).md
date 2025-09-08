```dataview
table dateformat(file.mtime, "yyyy-MM-dd") as "Last Modified"
from "Educational"
where file.mtime
and !contains(file.path, "Educational/Meta")
sort file.mtime asc
```