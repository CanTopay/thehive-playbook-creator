# thehive-playbook-creator
A script to create and assign SOP tasks dynamically to the cases.

# WHY
TheHive has built-in case templates functionality, which you can use with predefined case bindings. But I found it a bit tricky/hard to manage when working with multiple incident sources with endless possible customizations. Therefore I made this simple SOP creation script. Using this approach, you can build advanced methods that you can dynamically create and assign your playbooks by types of alarms or correlation rules you have, from any case post method. (Siem, workflow engine, etc.)
To make it clearer; I prepared a sample playbook with potential incident response actions to the first Mitre Tactic("Initial Access") and all techniques under that.
Use this sample script to build your integration method for your alerts/incidents; add your flavor of incident response procedures into the Json file in order; or add the remaining items for Mitre tactics & techniques etc.. and there you have a dynamic SOP library!

# NOTES
I used a json file to define and sort all playbook items/tasks in order. The top leading group is for default tasks; see first "Default" tasks group followed by more particular groups of incident response tasks for more certain rule/alarm types. This usage gives you the possibility to map an incident into a default catch group first. And if you have more rules(alerts) contributing to that case (2 or more supported), which makes it more precise, you can also specify more detailed incident response steps for them.
You will see the entries on theHive at the order that you wrote them into the json file. So keep the file in the order you like.
And another benefit might be for devops approach; using this json based playbook with Git and dev pipelines, you can monitor and manage changes with your code branches and also apply for approvals before any push to your main branch - which is your SOP/Playbook.

# Json file
![Json in order](Screenshot-JsonFile.png)
.
.
.

# TheHive
![Tasks screen on theHive](Screenshot-thehive.png)
