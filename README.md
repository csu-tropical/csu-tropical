# Documentation for the tropical website maintainance
url: tropical.colostate.edu AND bell.atmos.colostate.edu

### Research and Publication documented by Ting-Yu Cha 06/02/2020


## Publication: publication.html

### Structure of publication page:
Full list of publications (code can be found: _includes/full_list_publications.html)
Three categories: submitted/In review, in press, and published papers
_data/publication_submitted.yml: stores the manuscripts are submitted or in review
_data/list_long.yml: stores the papers are in press, published and passed first round of review (i.e. Ting-Yu’s GRL paper has passed the first round of review, so the content can be revealed online)
That being said, the info of Ting-Yu and Chelsea’s papers are both stored in _data/publication_submitted.yml and _data/list_long.yml.
If the paper gets published, remove the info from publication_submitted.yml, and add/modify new content in _data/list_long.yml.
Publications prior to 2019 are still hard-coded and are without a yaml file. The code can be found: _includes/full_list_publications.html
Book chapters/Sidebars/Thesis
Hard coded, the code can be found: _includes/book_sidesbars_others_publications.html

### Publications sorted by Authors
The sorting function can be found in publication.html using _data/members.yml to generate pages for each member. 
One thing to note is that the id (last name) in _data/members.yml is the key to sort out the research, publication, and research_group page. Make sure to modify the _data/members.yml if anyone joins our group or leaves.
The publication list of each member is generated from: _layouts/member_publications.html

### Publications sorted by Keywords 
The keywords list is under: _data/keywords.yml. One thing to note is that the research index card and publications share the same keywords.yml file. So please make sure the keywords in research index cards and publications are denoted in the keywords.yml file.
One possible way to get all keywords from the list_long.yml is by running the command in the terminal: yq r list_long.yml --collect .keyword* > keywords.yml (install yq by running: brew install yq on the command line). This command is very convenient as a starting point when there is no keywords.yml, but I will not recommend to do that now since there are multiple overlaps of keywords between publications and this command doesn’t trim down the keywords if appearing multiple times. I will recommend manually editing keywords.yml for future publications and research if any of the keywords is missing is the keywords.yml file.
Adding new publications: 
Decide whether the publication is In review/submitted, in press, or being published by .others in the yaml file
.others: submitted (no content will be revealed on the website) 
.others: In review (a sub-page will be generated, for papers have passed first round of review)
.others: in press (a sub-page will be generated)
.others: volume, pages etc (a published paper will normally have)
Add new content in the _data/publication_submitted.yml for submitted manuscript
.others has to be either submitted (no content will be revealed on the website) or In review (a sub-page will be generated).
Add new content in the _data/list_long.yml for in press, published manuscripts, and submitted manuscript which has passed the first round of review.
.others has to be in press for in press manuscripts.
Make sure to remove the paper gets published in the _data/publication_submitted.yml
Other content:
Paper folder: Publications/papers/
Bibtex folder: Publications/bibtex/
Figure folder: Publications/figures/
Book chapters, sidebars: Publications/bookchapters/
Sidebars: Publications/sidebars/
Thesis: Publications/thesis/



## Research: research.html
### Structure of research page:
For now the research projects are grants-based. The research projects can be found in _data/research_projects.yml, and we have 6 projects.
The sub-pages for each research project are generated from _layouts/projects.html, and the research index cards are produced by _data/research/index_card.yml. The layout of research index card can be found: _layouts/index_card.html
Research index cards sorted by keywords are generated from _layouts/keywords_projects.html. As mentioned before, the pages are generated based on _data/keywords.yml, so make sure to double check this yaml file to see if keywords in the research index cards are in the yaml file.
The research project list of each member is generated from _layouts/member_research.html

### Adding new research index card
Add the new content to the _data/research/index_card.yml file. I’d recommend directly appending the new content to the yaml file because most of the yaml files I received so far have some issues, and I have to manually edit those files to prevent jekyll build crash.
If jekyll build crashes, the most likely reason is the incorrect format of yaml files. 
Make sure the url of each member points to the right location using their last name (should be consistent with the _data/members.yml id). For example: member1: Ting-Yu Cha, and url1: ../research_group.html#cha
The name of member should be consistent with the full_name in _data/members.yml
Other content:
Oral folder: Research/oral/
Poster folder: Research/poster/
Figure folder: Research/img/
Publication: /pub/[html created by the publication functions, should be consistent with the id in the list_long.yml]

### General comments for research and publication:
All the research and publication blank and example files can be found in the example_yaml folder.
Yaml files are case sensitive, so make sure the keywords in research index card and publication are consistent with the keywords.yml
If there is a colon (:) in the parameter, make sure to add > , and press enter and tab (or space), like the figure showing below.

<img src="/images/YAML_example_doc.png"
     alt="YAML_example_doc.png"
     style="float: center; margin: 10px;" />

