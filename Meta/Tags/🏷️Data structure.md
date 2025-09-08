```dataview
table dateformat(file.mtime, "yyyy-MM-dd") AS "Last Modified"
from [[]]
where contains(file.outlinks, this.file.link)
sort file.mtime asc
```