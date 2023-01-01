
This script takes a directory path that should include images (hardcoded right now) and then outputs a text file with the a list of shortcodes that can be copy and pasted to Hugo site.


Running the script:

```
python3 scriptv1.py ./mypics outputNew.txt
```


Example output

```
{{<imageToClickGlobal imgPosition = "left"  imagePath = "/img/DALL·E 2022-12-29 23.47.10 - Warriors walking across a ice bridge where shattered ice is breaking from boulders.png" Capition = "DALL·E 2022-12-29 23.47.10 - Warriors walking across a ice bridge where shattered ice is breaking from boulders.png"  width = "60%" >}}
```