# Big data exploration

This is what we have and we continue to do this for the next deadline you will give. Hopefully it will be after the exams, and we will submit our write up in [./report] folder as well.

## Dataset Generating
The Plan is to generate a dataset with following form:

Username|Password|Password(md5 encrypted)|Messenges
---|---|---|---
xihajun|12345678|efw234rfdxfYIGUD|Some Fraud or ad
...|...|...|...

It is easy to do. Say we have a system with a big dataset, but it can be small in our simulation.
- [ ] We need to send messenges when user login. And encrypt the users' messenges 
Plan can be find some unmached password. Count the top frequent words in messenges. 

Labelled Fraud or ad SMS and count the word or do prediction.

Encode Messenges
## 
# TODO list
- [x] Select the encoding techniques 
  - Fernet(chosen) file2binary and encode binary
- [x] Do encoding and decoding work (maybe different sizes)
  - [x] Trying different number of files (linear increasing)
  - [ ] Try different length of string
- [ ] Read some papers about cryptography and parallel
- [ ] ...
