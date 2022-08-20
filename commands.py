import os

class Commands:

	@staticmethod
	def help(command):
		content = f'<p>term@<span>site:$ ~</span> <fore>{command}</fore></p><e><p style="margin-bottom: 17px" >Help has arrived!<br><br>whoami<br>clear/cls<br>reload<br>about<br>github<br>help</p></e>'
		return content

	@staticmethod
	def github(command):
		content = f'<p>term@<span>site:$ ~</span> <fore>{command}</fore></p><e><p><a href="https://github.com/Sebastian09-09/Termsite" target="_blank" >Link to the Github repo ↗</a></p><p style="margin-bottom: 17px" >Make sure to leave a star !</p></e>'
		return content

	@staticmethod
	def about(command):
		content = f'<p>term@<span>site:$ ~</span> <fore>{command}</fore></p><e><p>Termsite - The Terminal Website </p><p>Addicted to using Terminals?<br>Don\'t worry i have got you covered!</p></e>'
		return content

	@staticmethod
	def whoami(command):
		content = f'<p>term@<span>site:$ ~</span> <fore>{command}</fore></p><e><p>Sebastian</p></e>'
		return content

	@staticmethod
	def empty():
		content = f'<p style="margin-bottom: 17px" >term@<span>site:$ ~</span></p>'
		return content