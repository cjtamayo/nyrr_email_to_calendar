#!/usr/bin/env bash
echo starting nyrr to email run
echo changing email file name

cd email_loc
for file in *.eml; do
    mv "$file" "nyrr_email.eml"
done

echo complete with name change

cd ..

echo running script
python3.7 worker.py

echo deleting eml file
cd email_loc
rm nyrr_email.eml

echo COMPLETE
