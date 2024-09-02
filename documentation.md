# Documentation for the tropical website maintainance
[link to the website](tropical.colostate.edu)

* Order: 1. Home, 2. News, 3. Team member, 4. Forecasting, 5. Publication, 6. Research, and 7. Deployment
* This documentation does not explain every bit of the website and it focuses on the maintenance of the website - adding and removing contents 
* For testing the staging branch: http://taku.atmos.colostate.edu:8080 (you need to use secure.colostate.edu if you are logging in outside of CSU network)

* Written by
     - Research and Publication documented by Ting-Yu Cha 06/02/2020
     - Home, News, Team member, and Forecasting documented by Chelsea Nam 06/04/2020



## 1. Home: index.html
### structure of Home page
* Banner 
     - Banner images are stored in /images/banner folder
     - The maximum number of banner slide is 6.
     - To replace or add image in the banner put the image file in the /images/banner folder, and put them in <img src=” /images/banner/YOUR_IMAGE_FILE”>
     - Change the hyperlink and the header as you wish.
* Pop-up box (for new seasonal forecast release)
     - Turn on and off the pop-up box function by changing *style=”display:block”* to *style=”display:none”*
     - Change the header(starting with <h3 style=) and the content of the pop-up box (starting with <p style=”text-align:center) accordingly.
* Forecast and Research Buttons 
* News section
     - This section is automatically generated through Jekyll Liquid code based on the list of news posts in /_post/ folder. You can just add a post and figure and the home page will show the 3 most recent posts.
* Research gallery
     - The image of the research gallery photos should be in 16:9 ratio.
     - The images are to be stored in /images/gallery folder.
     - Change the hyperlink and the header, and the images.
     - Note that both the header and the images should be hyperlinked.
* Footer
     - They are controlled by htmls in _layout to change things in the footer go /_layout/
     - To change the text in the footer go to/_layout/ folder, and change all the five files (default.html, default_group.html, default_member.html, default_popup.html, default_withdata.html) 
     - It’s commented as “<-- Footer -->”.

## 2. News: news.html
This page automatically generates the list of the news posts reading the *_post* folder.

### Add a news item

1. Prepare an image for the news item and put in in */images/news/* folder.
2. Copy a markdown file in the _post folder.
3. Rename the file as “yyyy-mm-dd-YOUR-NEW-TITLE.markdown”
4.Change the tags of [image, title, and author] accordingly.
5. Note the html code of <img />. Change the image source there, and you can move the location of code.
6. “<-- more -->” indicates where to break for the post excerpt. Make sure you put about one paragraph above the “<-- more -->” indicator to avoid the breakdown of the format of the news list.
7. Check both of the news post and the news list to make sure everything looks good.


## 3. Team Member: /research_group.html

### structure of Team Member page
- Using “group” layout (/_layout/group.html): Group layout is based on the default layout but it contains the CSS elements specific to thumbnails and the group photo slider. 
- Big chunks:
     - The first thing below the header is the photo slider for the group photos. You display the most recent three group photos there.
     - The second section is the thumbnails, clickable by viewers and it directs them to each member’s bio section.
     - The third and last section is the bio section.

### You have a new group photo to add
1. Make the new photo 16:9 ratio (important! Otherwise, the photo slider ratio will go very ugly)
2. Add the image file (.jpg or .png) onto /Group folder
3. Go to line #32 OR <div class=”slideshow-container”> 
4. Replace the oldest one with the second oldest one (the third one is deleted and the second one replaces the third one), and replace the second one with the first one.
5. Now put the information of the figure in the first one. 
  <img src="/images/group_example_documentation.png"
     alt="group_example_documentation.png"
     style="float: center; margin: 10px;" />   
6. Change the red underlined section with the name of the new image file.
7. Change the caption (blue underlined) accordingly.
8. You may want to replace the group photo on the home page banner as well. Go to index.html to make that change.

### Add a new member
1. Let the member provide the yaml file (you can find the sample yaml file in /_data/member/PI/michael.yml) and a head-shot profile
     - The head-shot profile photo has to be square, if not the ratio will look awkward.
     -  For the items in the yaml file: 
          - id is your surname with small letters
          - If you don’t have webpage or other contacts then put “webpage: false” 
          - Bio should be 5-7 sentence long, otherwise the layout of the team member webpage could go off.
2. Add the headshot photo in the /Group folder.
3. cd into the _data/member/ folder and place the yaml file in the appropriate folder of either /RA, /RS, or /students. RA is for Research Associate, and RS is for Research Scientist.
4. So, this is the most tricky part! Thumbnail!
     - The thumbnail is in the alphabetical order of surnames once it’s sorted out by the job titles.
     - Each image takes 1/12 of the space. 
     - For now, I put the blank image for the first slot, and you mark the end of the row with <div class=”1u$>
     - So, copy the four lines of code starting from <div class=”1u”> OR <div class=”1u$”> and replace the image and the figure caption.
     - Be sure to check if the final layout is looking good and center-aligned.

### Move a member to alumni section
1. Move the yaml file for the member to /_data/member/alumni folder. 
2. Add time, thesis and job tag referring to the other yaml files in the folder.
3. Delete the person from the thumbnail section
     - Delete the four lines of code starting from <div class=”1u”> OR <div class=”1u$”> for that member.
     - If that person’s thumbnail was on the first row, you’d want to move one person in the second row to the first row. 
     - Each image takes 1/12 of the space. 
     - For now, I put the blank image for the first slot, and you mark the end of the row with <div class=”1u$>
     - Be sure to check if the final thumbnail layout is looking good and center-aligned.

### Update a member’s info
- Update the person’s yaml file in _data/member folder
- If needed, update the figure caption of the thumbnail photos
- Replace the headshot image with a new file (it will transfer smoothly if you keep the same name for the image file)

## 4. Forecasting: /forecasting.html

### Add new seasonal forecast released
1. Add the pdf file to /Forecast/
2. Go to _data/archive/2020s.yml and add the name of the pdf file there.
3. Write a news item for the new forecast
4. Change the Pop-up box accordingly (go to Home page documentation)
5. Change the current.yml file in _data/forecasting directory with the number form the current forecast
6. Change the paragraphs below the current forecast table accordingly.
7. Make sure you turn off the forecast pop-up box sometime later

### ARCHIVE (/archive.html): Update the data
- Update AMO index in  _data/forecasting/csu_amo.csv, also update .csv file for download in Forecast/downloadable/csu_amo.csv
- Update Verification data in _data/forecasting/verification. The files are sorted by each TC parameter in separate .csv
- Update TC stat data in _data/forecasting/stat folder. The files are sorted by basins named as archive_NA.csv, archive_WNP.csv etc

### RESOURCES (/resources.html): 
- Add new CSU resources: go to /_include/CSU_resources.html to add new stuff
- Add new external resources link: go to /_inlcue/external_resources.html to change the link or add a new link
- Add FAQ item: go to /_include/faq.html 


## 5. Publication: publication.html

### Structure of publication page:
- Full list of publications (code can be found: _includes/full_list_publications.html)
     - Three categories: submitted/In review, in press, and published papers
     - _data/publication_submitted.yml: stores the manuscripts are submitted or in review
     - _data/list_long.yml: stores the papers are in press, published and passed first round of review (i.e. Ting-Yu’s GRL paper has passed the first round of review, so the content can be revealed online)
     - That being said, the info of Ting-Yu and Chelsea’s papers are both stored in _data/publication_submitted.yml and _data/list_long.yml.
     - If the paper gets published, remove the info from publication_submitted.yml, and add/modify new content in _data/list_long.yml.
     - Publications prior to 2019 are still hard-coded and are without a yaml file. The code can be found: _includes/full_list_publications.html
- Book chapters/Sidebars/Thesis
     - Hard coded, the code can be found: _includes/book_sidesbars_others_publications.html

# Publication Update Instructions

Load Jekyll on the machine you will be using to update the webpage
	https://jekyllrb.com/docs/installation/

Clone the ‘staging branch’ to your local machine using the commands:
> git clone https://github.com/mmbell/csu-tropical.git
> cd csu-tropical
> git checkout staging

Make changes to files as follows:

For New Submissions:
 Run script ‘publication_submitted.yml’ and fill in requested fields (script is located under the main directory)
 Note:(1) '1st, 2nd, 3rd authors' must only be Bell group members, 'all_authors may include external authors)
(2) paper status is either 'submitted', 'in press' or you provide the volume number and issue number (ie vol 15, issue 2)


For Accepted Publications:
If remotely accessing publications from a Journal with restricted access you can click https://lib.colostate.edu/
Enter publication title
Download PDF, bibtex file and one key figure to highlight

Add PDF’s to /Publications/papers
Add image file to /Publications/figures
Add bibtex file to /Publications/bibtex
Run script ‘create.yml.published.py’ to create a new YAML file (script is located under the main directory)
Notes:
(1) '1st, 2nd, 3rd authors' must only be Bell group members, 'all_authors may include external authors)
(2) paper status is either 'submitted', 'in press' or you provide the volume number and issue number (ie vol 15, issue 2)
(3) Abstract, Summary, Figure Caption and Aknowledgment may be too long to enter using script. These may neeed to be added after YAML files is created. 

Once the file has been created you can copy and paste in the abstract and plain language summary (these are often too long to paste correctly into the file using the python script). 
Add the YAML file to _data/list_long.yml
Remove the YAML from _data/publication_submitted.yml


After all changes have been made run the following command to ensure the website displays correctly.
> bundle exec jekyll serve

If all looks good then you can merge your changes back to the staging tree. From the directory ‘csu-tropical’
> git branch #tells which branch you're in
> git add .
> git push
> git commit



### Publications sorted by Authors
- The sorting function can be found in publication.html using _data/members.yml to generate pages for each member. 
- One thing to note is that the id (last name) in _data/members.yml is the key to sort out the research, publication, and research_group page. Make sure to modify the _data/members.yml if anyone joins our group or leaves.
- The publication list of each member is generated from: _layouts/member_publications.html

### Publications sorted by Keywords 
- The keywords list is under: _data/keywords.yml. One thing to note is that the research index card and publications share the same keywords.yml file. So please make sure the keywords in research index cards and publications are denoted in the keywords.yml file.
- One possible way to get all keywords from the list_long.yml is by running the command in the terminal: yq r list_long.yml --collect .keyword* > keywords.yml (install yq by running: brew install yq on the command line). This command is very convenient as a starting point when there is no keywords.yml, but I will not recommend to do that now since there are multiple overlaps of keywords between publications and this command doesn’t trim down the keywords if appearing multiple times. I will recommend manually editing keywords.yml for future publications and research if any of the keywords is missing is the keywords.yml file.
- Adding new publications: 
     - Decide whether the publication is In review/submitted, in press, or being published by .others in the yaml file
          * .others: submitted (no content will be revealed on the website) 
          * .others: In review (a sub-page will be generated, for papers have passed first round of review)
          * .others: in press (a sub-page will be generated)
          * .others: volume, pages etc (a published paper will normally have)
- Add new content in the _data/publication_submitted.yml for submitted manuscript
     - .others has to be either submitted (no content will be revealed on the website) or In review (a sub-page will be generated).
- Add new content in the _data/list_long.yml for in press, published manuscripts, and submitted manuscript which has passed the first round of review.
     - .others has to be in press for in press manuscripts.
- Make sure to remove the paper gets published in the _data/publication_submitted.yml
- Other content:
     - Paper folder: Publications/papers/
     - Bibtex folder: Publications/bibtex/
     - Figure folder: Publications/figures/
     - Book chapters, sidebars: Publications/bookchapters/
     - Sidebars: Publications/sidebars/
     - Thesis: Publications/thesis/



## 6. Research: research.html
### Structure of research page:
- For now the research projects are grants-based. The research projects can be found in _data/research_projects.yml, and we have 6 projects.
- The sub-pages for each research project are generated from _layouts/projects.html, and the research index cards are produced by _data/research/index_card.yml. The layout of research index card can be found: _layouts/index_card.html
- Research index cards sorted by keywords are generated from _layouts/keywords_projects.html. As mentioned before, the pages are generated based on _data/keywords.yml, so make sure to double check this yaml file to see if keywords in the research index cards are in the yaml file.
- The research project list of each member is generated from _layouts/member_research.html

### Adding new research index card
- Add the new content to the _data/research/index_card.yml file. I’d recommend directly appending the new content to the yaml file because most of the yaml files I received so far have some issues, and I have to manually edit those files to prevent jekyll build crash.
- If jekyll build crashes, the most likely reason is the incorrect format of yaml files. 
- Make sure the url of each member points to the right location using their last name (should be consistent with the _data/members.yml id). For example: member1: Ting-Yu Cha, and url1: ../research_group.html#cha
- The name of member should be consistent with the full_name in _data/members.yml
- Other content:
     - Oral folder: Research/oral/
     - Poster folder: Research/poster/
     - Figure folder: Research/img/
     - Publication: /pub/[html created by the publication functions, should be consistent with the id in the list_long.yml]

### General comments for research and publication:
- All the research and publication blank and example files can be found in the example_yaml folder.
- Yaml files are case sensitive, so make sure the keywords in research index card and publication are consistent with the keywords.yml
- If there is a colon (:) in the parameter, make sure to add > , and press enter and tab (or space), like the figure showing below.

<img src="/images/yaml_example_documentation.png"
     alt="yaml_example_documentation.png"
     style="float: center; margin: 10px;" />

## 7. Deployment
- The website is hosted on a WSCOE server called 'engr.colostate.edu' accessible via Samba network mount: smb://www.engr.colostate.edu/atmos-www/bell 
- In webmaster's home directory, there are 2 scripts called 'stage.sh' and 'deploy.sh'. Both scripts are automated and perform the following actions: 
     1. Pull down the latest content from GitHub on either the staging (stage) or master (deploy) branch
     2. Run the getglobaltcdata.sh script to get the latest real-time TC stats and update the data files
     3. Run jekyll build in the production environment
     4. Rsync any updated files from \_site subdirectory to the atmos-www/bell network mount
- The deploy script is run automatically 4 times per day at 3, 9, 15, and 21 MDT via cron to provide automated updates of the TC stats
- Manual updates should be tested first using the 'stage' script which will deploy to the staging nginx server at http://taku.atmos.colostate.edu:8080 which is only accessible to internal CSU viewers via VPN.
- Note that webmaster has 'read-only' access to the csu-tropical repository on GitHub. It is not a full GitHub user account, just a simple deploy account that has ssh read-only access. That account can't be used to make content changes, only to stage or deploy content that has already been committed and pushed to GitHub by another (full) user.
- If all looks good with the staging, then under your own user account (not webmaster) merge the staging branch to master ('git checkout master' then 'git merge staging'). As webmaster, run the deploy script.
