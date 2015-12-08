def make_links_table(s):
    table_html = """<table>
  <tr>
    <td>User</td>
    <td>Sound</td>
  </tr>"""
    while len(s) > 30:
        x = s.find("User:")
        y = s.find("sound:")
        user = s[x+6:y-2]
        w = s.find("<a href")
        z = s.find("<br>")
        sound = s[w:z]
        s = s[z+2:]
        table_html += """
  <tr>
    <td>""" + user + """</td>
    <td>""" + sound + """</td>
  </tr>"""
    table_html += """
</table>"""
    return table_html


old_links = """User: Quistard, sound:
            <a href="https://www.freesound.org/people/Quistard/sounds/166838/">166838</a><br>
            User: hisoul, sound:
            <a href="https://www.freesound.org/people/hisoul/sounds/255341/">255341</a><br>
            User: Soughtaftersounds, sound:
            <a href="https://www.freesound.org/people/Soughtaftersounds/sounds/145416/">145416</a><br>
            User: poorenglishjuggler, sound:
            <a href="https://www.freesound.org/people/poorenglishjuggler/sounds/269496/">269496</a><br>
            User: pulswelle, sound:
            <a href="https://www.freesound.org/people/pulswelle/sounds/175295/">175295</a><br>
            User: fer_t, sound:
            <a href="https://www.freesound.org/people/fer_t/sounds/94295/">94295</a><br>
            User: Timbre, sound:
            <a href="https://www.freesound.org/people/Timbre/sounds/70105/">70105</a><br>
            User: hanuman81, sound:
            <a href="https://www.freesound.org/people/hanuman81/sounds/170652/">170652</a><br>
            User: f4ngy, sound:
            <a href="https://www.freesound.org/people/f4ngy/sounds/240784/">240784</a><br>
            User: gerfaut83, sound:
            <a href="https://www.freesound.org/people/gerfaut83/sounds/185633/">185633</a><br>
            User: leosalom, sound:
            <a href="https://www.freesound.org/people/leosalom/sounds/234879/">234879</a><br>
            User: SquaredGlasses, sound:
            <a href="https://www.freesound.org/people/SquaredGlasses/sounds/253649/">253649</a><br>
            User: Dann93, sound:
            <a href="https://www.freesound.org/people/Dann93/sounds/192035/">192035</a><br>
            User: dobroide, sound:
            <a href="https://www.freesound.org/people/dobroide/sounds/161925/">161925</a><br>
            User: reinsamba, sound:
            <a href="https://www.freesound.org/people/reinsamba/sounds/259099/">259099</a><br>
            User: tobyf, sound:
            <a href="https://www.freesound.org/people/tobyf/sounds/105003/">105003</a><br>
            """
print make_links_table(old_links)