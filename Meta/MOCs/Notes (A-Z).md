```dataview
table dateformat(file.mtime, "yyyy-MM-dd") as "Last Modified"
from "Educational"
where !contains(file.path, "Educational/Meta")
sort file.name asc
```