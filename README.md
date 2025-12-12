# cybersecurity_notes

These are the cybersecurity notes I made while studying for the CompTIA Security+. I figured it would make studying less monotonous if I created a scalable resource simultaneously.

The notes are in pure markdown format and follow a pretty rigid structure that I decided upon: title -> tags -> paragraph -> bullet points -> paragraph -> related notes. There are exceptions if I decided a certain note should be more detailed. Various LLM's were used to write the notes in a way that makes sense to me for easy reviewing and memorizing.

I've employed various techniques to keep the growing amount of notes manageable. First I should talk about a technique that I tried but ultimately did not stick with: the [Johnny Decimal](https://johnnydecimal.com/) system. This uses a simple numbering system dividing everything into 10 main categories and each category is divided into 10 subcategories. Notes go inside these subcategories and are givin a unique number for indexing.

My issues with this were:

1. Decision fatigue: I often felt less inclined to make notes because I had to decide where to put them in the system.

2. Overlap issues: Some notes naturally fit into multiple areas (especially in cybersecurity), and the systems rigid single-place indexing made it hard to organize them.

I've favored a more flat/networked style of organization. All notes go in one directory. Simple. No friction. To manage this I use links, tags, dataview queries and the Obsidian search function. This way any single note can belong to multiple categories at once creating a sort of network of interconnected ideas.

I've decided to keep links out of the main content area in notes because all of the linking sytax gets messy and annoying to deal with when working with notes in markdown view.

Images by default are just linked onto the notes you want the images on which is advantageous because it keeps the note files lightweight and allows the reuse of a single image an artibtrary amount of times throughout your notes. I wanted this flexibility/scalability with my tables and diagrams aswell so they also reside in separte notes that are just linked to. This is escpecially useful because I can change a table or diagram once and that change reflects throughout all notes that display this data. The images, tables and diagrams all follow a basic numbering system Image 1.00, Image 1.01, Image 1.02, etc... I made python scripts to show me which image, tables, diagrams are present in my vault but are not being used. Interestingly, when I find unused data instead of deleting them right away, I keep them but keep note that next time I add a new image for example, it should take over that unused ones numbering slot, then I delete the unused one. I do this to maintain the numbering system and to avoid numbering gaps.

<!-- CODE_STATISTICS_START -->

### Code Statistics

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Markdown                      1259          10437              4          17562
Python                           3             31             36            103
-------------------------------------------------------------------------------
SUM:                          1262          10468             40          17665
-------------------------------------------------------------------------------
```
<!-- CODE_STATISTICS_END -->

<!-- PROJECT_STRUCTURE_START -->

### Project Structure

```
```
<!-- PROJECT_STRUCTURE_END -->

