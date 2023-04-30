# 'Yelverton Bowmen' Website Prototype

---

## Overview

I used Python's `Flask` module to create a dynamic website for Yelverton Bowmen. This website is only meant to be a prototype that I can use to develop my knowledge regarding Front-End Development for my position at the club as Webmaster.

---

## What is Flask?

> A Web Application Framework or a simply a Web Framework represents a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management, and so on.

> Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine.

Flask uses HTML 'Jinja2' templates mixed in with Python code to deliver dynamic, user-specific content.

> jinja2 is a popular template engine for Python. A web template system combines a template with a specific data source to render a dynamic web page.

```html
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>Hello {{ username }}</h1>
    </body>
</html>
```

---

## Where Flask Was Used in This Project?

### 'Committee Members' Section 

[club.html](/yelverton_bowmen/templates/club.html)

This section iterates through the `name` and `role_info` items in the dictionary `committee_members`  found in [commitee.py](/yelverton_bowmen/commitee.py). <br>
It then displays this information in a table containing an image, the role title, the committee members name and a description of the role.

```html
<div id="committee">
    <h2>Committee</h2>
    <p>The Yelverton Bowmen committee is elected each year at the AGM. The current committee is listed below.</p>
    
    {% for name, role_info in committee_members.items() %}
    <div class="committee-member">
        <table>
            <tr>
                <td>
                    <img src="{{role_info[1]}}" />
                </td>
                <td>
                <h3>{{ role_info[0] }}</h3>
                <p><i>{{ name }}</i></p>
                <p>{{ role_info[2] }}</p>
                </td>
            </tr>
        </table>
        <br>
    </div>
    {% endfor %}
</div>
```

```py
committee_members = {

        "Linda Wright" : 
            ["Chairman", 
             "static/imgs/committee-members/chairman.jpg", 
             "The Chairman is the ‘manager’ of the club and the committee. They lead committee meetings and are responsible for coordination of committee tasks."] ,

             ...

}
```

![committee-members-section](/yelverton_bowmen/readme_assets/committee-section.png)

### Club Records

```py
from static.records.barebow import barebow
from static.records.recurve import recurve
from static.records.compound import compound
from static.records.longbow import longbow
from static.records.afb import afb
```

```py
@app.route('/records/<bowtype>')
def bowtype_record(bowtype):
    match bowtype:
        case "afb":
            bowtype=afb
        case "barebow":
            bowtype=barebow
        case "compound":
            bowtype=compound
        case "longbow":
            bowtype=longbow
        case "recurve":
            bowtype=recurve
        case _:
            bowtype=barebow
    return render_template("bowtype_record.html",
                           bowtype=bowtype)
```

- Pass in a bowtype via the URL.
- Check if bowtype matches from list, if it does select that imported dictionary.
- If the bowtype doesn't match from any of the selected items, default to 'barebow'.

```html
    <table>
        <tr>
            <th colspan="5">{{ bowtype[0] }}</th>
        </tr>
        <tr>
            <th rowspan="2">Round</th>
            <th colspan="2">Gents</th>
            <th colspan="2">Ladies</th>
        </tr>
        <tr>
            <th>Archer</th>
            <th>Score</th>
            <th>Archer</th>
            <th>Score</th>
        </tr>
        {% for round_name, record_data in bowtype[1].items() %}
        <tr>
            <td>{{ round_name }}</td>
            {% for i in range(0,4) %}
            <td>{{ record_data[i] }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
```

- Create a table.
- First row should be the bowtype name, spanning all columns.
- `<th colspan="5">{{ bowtype[0] }}</th>`
- The next row should consist of the 'Round' header spanning two rows and the 'Gents' and 'Ladies' headers.
- On the following row, display the 'Archer Name' and 'Score' headers for each gender.
- Now, iterate through the records dictionaries. These will be in the following format:
- `"round_name" : ["gents_archer_name", "gents_archer_score", "ladies_archer_name", "ladies_archer_score"] , `

![](/yelverton_bowmen/readme_assets/club-records.png)