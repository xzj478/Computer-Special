Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fhand = open('mbox.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.startwith('From:'):
		print(line)

		
Traceback (most recent call last):
  File "<pyshell#5>", line 3, in <module>
    if line.startwith('From:'):
AttributeError: 'str' object has no attribute 'startwith'
>>> for line in fhand:
	line = line.rstrip()
	if line.startswith('From:'):
		print(line)

		
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: gsilver@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: antranig@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: ray@media.berkeley.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ray@media.berkeley.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: ray@media.berkeley.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: gopal.ramasammycook@gmail.com
From: gsilver@umich.edu
From: gsilver@umich.edu
From: stuart.freeman@et.gatech.edu
From: zqian@umich.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: wagnermr@iupui.edu
From: stuart.freeman@et.gatech.edu
From: tnguyen@iupui.edu
From: stuart.freeman@et.gatech.edu
From: wagnermr@iupui.edu
From: gopal.ramasammycook@gmail.com
From: ray@media.berkeley.edu
From: ray@media.berkeley.edu
From: zqian@umich.edu
From: wagnermr@iupui.edu
From: stuart.freeman@et.gatech.edu
From: chmaurer@iupui.edu
From: stuart.freeman@et.gatech.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: aaronz@vt.edu
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: wagnermr@iupui.edu
From: csev@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: rjlowe@iupui.edu
From: jimeng@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: gsilver@umich.edu
From: ian@caret.cam.ac.uk
From: csev@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: josrodri@iupui.edu
From: josrodri@iupui.edu
From: csev@umich.edu
From: ian@caret.cam.ac.uk
From: csev@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: knoop@umich.edu
From: knoop@umich.edu
From: knoop@umich.edu
From: knoop@umich.edu
From: knoop@umich.edu
From: cwen@iupui.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: csev@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: bkirschn@umich.edu
From: jimeng@umich.edu
From: ian@caret.cam.ac.uk
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: ian@caret.cam.ac.uk
From: jimeng@umich.edu
From: jimeng@umich.edu
From: ray@media.berkeley.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: stuart.freeman@et.gatech.edu
From: bkirschn@umich.edu
From: zqian@umich.edu
From: louis@media.berkeley.edu
From: dlhaines@umich.edu
From: bkirschn@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: bkirschn@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: bkirschn@umich.edu
From: bkirschn@umich.edu
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: stephen.marquard@uct.ac.za
From: david.horwitz@uct.ac.za
From: bkirschn@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: dlhaines@umich.edu
From: josrodri@iupui.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: hu2@iupui.edu
From: louis@media.berkeley.edu
From: bkirschn@umich.edu
From: josrodri@iupui.edu
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: josrodri@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: hu2@iupui.edu
From: cwen@iupui.edu
From: tnguyen@iupui.edu
From: sgithens@caret.cam.ac.uk
From: arwhyte@umich.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: david.horwitz@uct.ac.za
From: josrodri@iupui.edu
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: david.horwitz@uct.ac.za
From: dlhaines@umich.edu
From: stephen.marquard@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: zqian@umich.edu
From: zqian@umich.edu
From: gbhatnag@umich.edu
From: dlhaines@umich.edu
From: jimeng@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ray@media.berkeley.edu
From: rjlowe@iupui.edu
From: jimeng@umich.edu
From: wagnermr@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: wagnermr@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: stephen.marquard@uct.ac.za
From: gjthomas@iupui.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: jimeng@umich.edu
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: cwen@iupui.edu
From: gsilver@umich.edu
From: cwen@iupui.edu
From: stuart.freeman@et.gatech.edu
From: wagnermr@iupui.edu
From: stuart.freeman@et.gatech.edu
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: louis@media.berkeley.edu
From: gsilver@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: tnguyen@iupui.edu
From: cwen@iupui.edu
From: bkirschn@umich.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: tnguyen@iupui.edu
From: cwen@iupui.edu
From: tnguyen@iupui.edu
From: cwen@iupui.edu
From: dlhaines@umich.edu
From: cwen@iupui.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ajpoland@iupui.edu
From: josrodri@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: dlhaines@umich.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gsilver@umich.edu
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: cwen@iupui.edu
From: lance@indiana.edu
From: lance@indiana.edu
From: dlhaines@umich.edu
From: lance@indiana.edu
From: chmaurer@iupui.edu
From: ian@caret.cam.ac.uk
From: lance@indiana.edu
From: lance@indiana.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ajpoland@iupui.edu
From: cwen@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: stephen.marquard@uct.ac.za
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: ian@caret.cam.ac.uk
From: rjlowe@iupui.edu
From: wagnermr@iupui.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: louis@media.berkeley.edu
From: ian@caret.cam.ac.uk
From: wagnermr@iupui.edu
From: wagnermr@iupui.edu
From: gsilver@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: wagnermr@iupui.edu
From: stuart.freeman@et.gatech.edu
From: cwen@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: ssmail@indiana.edu
From: cwen@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: cwen@iupui.edu
From: wagnermr@iupui.edu
From: rjlowe@iupui.edu
From: dlhaines@umich.edu
From: jlrenfro@ucdavis.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: arwhyte@umich.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: nuno@ufp.pt
From: wagnermr@iupui.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: nuno@ufp.pt
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: cwen@iupui.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: rjlowe@iupui.edu
From: wagnermr@iupui.edu
From: gjthomas@iupui.edu
From: nuno@ufp.pt
From: wagnermr@iupui.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: zach.thomas@txstate.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: arwhyte@umich.edu
From: josrodri@iupui.edu
From: arwhyte@umich.edu
From: josrodri@iupui.edu
From: stephen.marquard@uct.ac.za
From: stephen.marquard@uct.ac.za
From: gjthomas@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: gjthomas@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: tnguyen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: mmmay@indiana.edu
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: cwen@iupui.edu
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: cwen@iupui.edu
From: bkirschn@umich.edu
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: cwen@iupui.edu
From: mmmay@indiana.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: lance@indiana.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: josrodri@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: david.horwitz@uct.ac.za
From: rjlowe@iupui.edu
From: sgithens@caret.cam.ac.uk
From: louis@media.berkeley.edu
From: louis@media.berkeley.edu
From: ktsao@stanford.edu
From: ray@media.berkeley.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: cwen@iupui.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: ostermmg@whitman.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: dlhaines@umich.edu
From: gopal.ramasammycook@gmail.com
From: jimeng@umich.edu
From: josrodri@iupui.edu
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: nuno@ufp.pt
From: wagnermr@iupui.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com
From: stuart.freeman@et.gatech.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: jimeng@umich.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: jimeng@umich.edu
From: zqian@umich.edu
From: cwen@iupui.edu
From: arwhyte@umich.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gjthomas@iupui.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: josrodri@iupui.edu
From: dlhaines@umich.edu
From: jimeng@umich.edu
From: dlhaines@umich.edu
From: jimeng@umich.edu
From: ray@media.berkeley.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: wagnermr@iupui.edu
From: cwen@iupui.edu
From: ssmail@indiana.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: josrodri@iupui.edu
From: sgithens@caret.cam.ac.uk
From: jimeng@umich.edu
From: jimeng@umich.edu
From: ktsao@stanford.edu
From: ray@media.berkeley.edu
From: ray@media.berkeley.edu
From: jimeng@umich.edu
From: louis@media.berkeley.edu
From: ktsao@stanford.edu
From: gbhatnag@umich.edu
From: ktsao@stanford.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gbhatnag@umich.edu
From: dlhaines@umich.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: josrodri@iupui.edu
From: josrodri@iupui.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: wagnermr@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: aaronz@vt.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: wagnermr@iupui.edu
From: gjthomas@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: aaronz@vt.edu
From: gjthomas@iupui.edu
From: zqian@umich.edu
From: josrodri@iupui.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: mmmay@indiana.edu
From: chmaurer@iupui.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: zqian@umich.edu
From: josrodri@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: ray@media.berkeley.edu
From: chmaurer@iupui.edu
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: rjlowe@iupui.edu
From: ian@caret.cam.ac.uk
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: aaronz@vt.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: chmaurer@iupui.edu
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: jimeng@umich.edu
From: chmaurer@iupui.edu
From: wagnermr@iupui.edu
From: josrodri@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: josrodri@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gopal.ramasammycook@gmail.com
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: ian@caret.cam.ac.uk
From: jimeng@umich.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: david.horwitz@uct.ac.za
From: gopal.ramasammycook@gmail.com
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gopal.ramasammycook@gmail.com
From: a.fish@lancaster.ac.uk
From: stuart.freeman@et.gatech.edu
From: stuart.freeman@et.gatech.edu
From: stuart.freeman@et.gatech.edu
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ian@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: david.horwitz@uct.ac.za
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gopal.ramasammycook@gmail.com
From: cwen@iupui.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: jimeng@umich.edu
From: mmmay@indiana.edu
From: jimeng@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: wagnermr@iupui.edu
From: mmmay@indiana.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: chmaurer@iupui.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: john.ellis@rsmart.com
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: stuart.freeman@et.gatech.edu
From: stuart.freeman@et.gatech.edu
From: zqian@umich.edu
From: jleasia@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: gopal.ramasammycook@gmail.com
From: dlhaines@umich.edu
From: sgithens@caret.cam.ac.uk
From: dlhaines@umich.edu
From: aaronz@vt.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: cwen@iupui.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: dlhaines@umich.edu
From: antranig@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: zach.thomas@txstate.edu
From: dlhaines@umich.edu
From: aaronz@vt.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: aaronz@vt.edu
From: ssmail@indiana.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ssmail@indiana.edu
From: zqian@umich.edu
From: stuart.freeman@et.gatech.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: stuart.freeman@et.gatech.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: cwen@iupui.edu
From: ian@caret.cam.ac.uk
From: dlhaines@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: gopal.ramasammycook@gmail.com
From: dlhaines@umich.edu
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: john.ellis@rsmart.com
From: john.ellis@rsmart.com
From: aaronz@vt.edu
From: cwen@iupui.edu
From: zqian@umich.edu
From: wagnermr@iupui.edu
From: aaronz@vt.edu
From: wagnermr@iupui.edu
From: gopal.ramasammycook@gmail.com
From: lance@indiana.edu
From: sgithens@caret.cam.ac.uk
From: ggolden@umich.edu
From: ggolden@umich.edu
From: cwen@iupui.edu
From: ggolden@umich.edu
From: ggolden@umich.edu
From: ggolden@umich.edu
From: ggolden@umich.edu
From: david.horwitz@uct.ac.za
From: antranig@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: antranig@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: david.horwitz@uct.ac.za
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: ian@caret.cam.ac.uk
From: gopal.ramasammycook@gmail.com
From: ian@caret.cam.ac.uk
From: david.horwitz@uct.ac.za
From: gopal.ramasammycook@gmail.com
From: antranig@caret.cam.ac.uk
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ray@media.berkeley.edu
From: ktsao@stanford.edu
From: sgithens@caret.cam.ac.uk
From: zqian@umich.edu
From: cwen@iupui.edu
From: antranig@caret.cam.ac.uk
From: zqian@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: antranig@caret.cam.ac.uk
From: antranig@caret.cam.ac.uk
From: ssmail@indiana.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: mmmay@indiana.edu
From: gopal.ramasammycook@gmail.com
From: aaronz@vt.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: ian@caret.cam.ac.uk
From: mmmay@indiana.edu
From: jimeng@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: lance@indiana.edu
From: sgithens@caret.cam.ac.uk
From: aaronz@vt.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: john.ellis@rsmart.com
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: ktsao@stanford.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: cwen@iupui.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: thoppaymallika@fhda.edu
From: chmaurer@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: chmaurer@iupui.edu
From: sgithens@caret.cam.ac.uk
From: chmaurer@iupui.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: sgithens@caret.cam.ac.uk
From: david.horwitz@uct.ac.za
From: zqian@umich.edu
From: sgithens@caret.cam.ac.uk
From: ajpoland@iupui.edu
From: cwen@iupui.edu
From: gsilver@umich.edu
From: sgithens@caret.cam.ac.uk
From: jimeng@umich.edu
From: zqian@umich.edu
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: bkirschn@umich.edu
From: antranig@caret.cam.ac.uk
From: antranig@caret.cam.ac.uk
From: zqian@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: gopal.ramasammycook@gmail.com
From: zqian@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: john.ellis@rsmart.com
From: ajpoland@iupui.edu
From: chmaurer@iupui.edu
From: antranig@caret.cam.ac.uk
From: antranig@caret.cam.ac.uk
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: antranig@caret.cam.ac.uk
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: gopal.ramasammycook@gmail.com
From: zqian@umich.edu
From: kimsooil@bu.edu
From: kimsooil@bu.edu
From: kimsooil@bu.edu
From: zqian@umich.edu
From: ostermmg@whitman.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: zqian@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: jimeng@umich.edu
From: ray@media.berkeley.edu
From: ostermmg@whitman.edu
From: josrodri@iupui.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: rjlowe@iupui.edu
From: antranig@caret.cam.ac.uk
From: antranig@caret.cam.ac.uk
From: josrodri@iupui.edu
From: zqian@umich.edu
From: rjlowe@iupui.edu
From: ian@caret.cam.ac.uk
From: antranig@caret.cam.ac.uk
From: zqian@umich.edu
From: wagnermr@iupui.edu
From: gsilver@umich.edu
From: gopal.ramasammycook@gmail.com
From: ajpoland@iupui.edu
From: wagnermr@iupui.edu
From: wagnermr@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ajpoland@iupui.edu
From: wagnermr@iupui.edu
From: wagnermr@iupui.edu
From: david.horwitz@uct.ac.za
From: ray@media.berkeley.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: ajpoland@iupui.edu
From: ostermmg@whitman.edu
From: cwen@iupui.edu
From: jimeng@umich.edu
From: josrodri@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: wagnermr@iupui.edu
From: hu2@iupui.edu
From: josrodri@iupui.edu
From: wagnermr@iupui.edu
From: rjlowe@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: ian@caret.cam.ac.uk
From: ajpoland@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: jimeng@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: rjlowe@iupui.edu
From: jimeng@umich.edu
From: sgithens@caret.cam.ac.uk
From: sgithens@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: ray@media.berkeley.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: cwen@iupui.edu
From: bkirschn@umich.edu
From: gsilver@umich.edu
From: john.ellis@rsmart.com
From: aaronz@vt.edu
From: bkirschn@umich.edu
From: gopal.ramasammycook@gmail.com
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: ajpoland@iupui.edu
From: aaronz@vt.edu
From: sgithens@caret.cam.ac.uk
From: aaronz@vt.edu
From: jimeng@umich.edu
From: ostermmg@whitman.edu
From: ostermmg@whitman.edu
From: jimeng@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: sgithens@caret.cam.ac.uk
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: gopal.ramasammycook@gmail.com
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: dlhaines@umich.edu
From: wagnermr@iupui.edu
From: aaronz@vt.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: wagnermr@iupui.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: kimsooil@bu.edu
From: kimsooil@bu.edu
From: aaronz@vt.edu
From: nuno@ufp.pt
From: arwhyte@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: ajpoland@iupui.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ajpoland@iupui.edu
From: wagnermr@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: sgithens@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: josrodri@iupui.edu
From: josrodri@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: josrodri@iupui.edu
From: zqian@umich.edu
From: arwhyte@umich.edu
From: rjlowe@iupui.edu
From: dlhaines@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: arwhyte@umich.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: josrodri@iupui.edu
From: gjthomas@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: sgithens@caret.cam.ac.uk
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: ray@media.berkeley.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: david.horwitz@uct.ac.za
From: antranig@caret.cam.ac.uk
From: ggolden@umich.edu
From: antranig@caret.cam.ac.uk
From: ggolden@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: david.horwitz@uct.ac.za
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: wagnermr@iupui.edu
From: rjlowe@iupui.edu
From: gopal.ramasammycook@gmail.com
From: david.horwitz@uct.ac.za
From: zqian@umich.edu
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: ray@media.berkeley.edu
From: hu2@iupui.edu
From: mmmay@indiana.edu
From: bkirschn@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: ray@media.berkeley.edu
From: ray@media.berkeley.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: csev@umich.edu
From: josrodri@iupui.edu
From: csev@umich.edu
From: zqian@umich.edu
From: bahollad@indiana.edu
From: aaronz@vt.edu
From: jzaremba@unicon.net
From: ajpoland@iupui.edu
From: aaronz@vt.edu
From: csev@umich.edu
From: rjlowe@iupui.edu
From: nuno@ufp.pt
From: nuno@ufp.pt
From: mmmay@indiana.edu
From: bkirschn@umich.edu
From: jimeng@umich.edu
From: bkirschn@umich.edu
From: bkirschn@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: john.ellis@rsmart.com
From: zqian@umich.edu
From: jzaremba@unicon.net
From: jimeng@umich.edu
From: bkirschn@umich.edu
From: bkirschn@umich.edu
From: bkirschn@umich.edu
From: bkirschn@umich.edu
From: zqian@umich.edu
From: ktsao@stanford.edu
From: mmmay@indiana.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: dlhaines@umich.edu
From: bkirschn@umich.edu
From: zqian@umich.edu
From: bkirschn@umich.edu
From: ray@media.berkeley.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: zach.thomas@txstate.edu
From: ostermmg@whitman.edu
From: bkirschn@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: wagnermr@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: zach.thomas@txstate.edu
From: wagnermr@iupui.edu
From: gsilver@umich.edu
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: hu2@iupui.edu
From: ajpoland@iupui.edu
From: wagnermr@iupui.edu
From: david.horwitz@uct.ac.za
From: zqian@umich.edu
From: jzaremba@unicon.net
From: cwen@iupui.edu
From: ktsao@stanford.edu
From: bahollad@indiana.edu
From: zach.thomas@txstate.edu
From: cwen@iupui.edu
From: ajpoland@iupui.edu
From: wagnermr@iupui.edu
From: wagnermr@iupui.edu
From: aaronz@vt.edu
From: sgithens@caret.cam.ac.uk
From: a.fish@lancaster.ac.uk
From: aaronz@vt.edu
From: david.horwitz@uct.ac.za
From: david.horwitz@uct.ac.za
From: zqian@umich.edu
From: jzaremba@unicon.net
From: zach.thomas@txstate.edu
From: jzaremba@unicon.net
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: john.ellis@rsmart.com
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: chmaurer@iupui.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: kimsooil@bu.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: kimsooil@bu.edu
From: nuno@ufp.pt
From: kimsooil@bu.edu
From: ajpoland@iupui.edu
From: chmaurer@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: ajpoland@iupui.edu
From: dlhaines@umich.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: wagnermr@iupui.edu
From: david.horwitz@uct.ac.za
From: jleasia@umich.edu
From: david.horwitz@uct.ac.za
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: cwen@iupui.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: kimsooil@bu.edu
From: mmmay@indiana.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: mmmay@indiana.edu
From: kimsooil@bu.edu
From: aaronz@vt.edu
From: dlhaines@umich.edu
From: zqian@umich.edu
From: mmmay@indiana.edu
From: dlhaines@umich.edu
From: cwen@iupui.edu
From: kimsooil@bu.edu
From: kimsooil@bu.edu
From: kimsooil@bu.edu
From: hu2@iupui.edu
From: zqian@umich.edu
From: kimsooil@bu.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: rjlowe@iupui.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: hu2@iupui.edu
From: dlhaines@umich.edu
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: gsilver@umich.edu
From: mbreuker@loi.nl
From: mbreuker@loi.nl
From: mbreuker@loi.nl
From: mbreuker@loi.nl
From: mbreuker@loi.nl
From: mbreuker@loi.nl
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: a.fish@lancaster.ac.uk
From: dlhaines@umich.edu
From: mbreuker@loi.nl
From: david.horwitz@uct.ac.za
From: zach.thomas@txstate.edu
From: jimeng@umich.edu
From: zqian@umich.edu
From: jzaremba@unicon.net
From: colin.clark@utoronto.ca
From: ray@media.berkeley.edu
From: ray@media.berkeley.edu
From: ray@media.berkeley.edu
From: ray@media.berkeley.edu
From: louis@media.berkeley.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: ajpoland@iupui.edu
From: wagnermr@iupui.edu
From: zqian@umich.edu
From: ktsao@stanford.edu
From: ray@media.berkeley.edu
From: aaronz@vt.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: bahollad@indiana.edu
From: aaronz@vt.edu
From: zqian@umich.edu
From: ray@media.berkeley.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: bahollad@indiana.edu
From: ray@media.berkeley.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: louis@media.berkeley.edu
From: zqian@umich.edu
From: ray@media.berkeley.edu
From: jzaremba@unicon.net
From: louis@media.berkeley.edu
From: rjlowe@iupui.edu
From: ajpoland@iupui.edu
From: ray@media.berkeley.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: ray@media.berkeley.edu
From: zqian@umich.edu
From: bkirschn@umich.edu
From: mbreuker@loi.nl
From: zqian@umich.edu
From: gsilver@umich.edu
From: louis@media.berkeley.edu
From: bkirschn@umich.edu
From: bkirschn@umich.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: zach.thomas@txstate.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ray@media.berkeley.edu
From: ktsao@stanford.edu
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: chmaurer@iupui.edu
From: ian@caret.cam.ac.uk
From: gjthomas@iupui.edu
From: gjthomas@iupui.edu
From: aaronz@vt.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: mbreuker@loi.nl
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: dlhaines@umich.edu
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: chmaurer@iupui.edu
From: chmaurer@iupui.edu
From: zqian@umich.edu
From: gjthomas@iupui.edu
From: gsilver@umich.edu
From: ian@caret.cam.ac.uk
From: ajpoland@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: zach.thomas@txstate.edu
From: ajpoland@iupui.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: gjthomas@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: dlhaines@umich.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: cwen@iupui.edu
From: ktsao@stanford.edu
From: aaronz@vt.edu

From: aaronz@vt.edu
From: gsilver@umich.edu
From: gsilver@umich.edu
From: zqian@umich.edu
From: jzaremba@unicon.net
From: aaronz@vt.edu
From: aaronz@vt.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: dlhaines@umich.edu
From: ajpoland@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: rjlowe@iupui.edu
From: dlhaines@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ian@caret.cam.ac.uk
From: aaronz@vt.edu
From: aaronz@vt.edu
From: ktsao@stanford.edu
From: ian@caret.cam.ac.uk
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: zqian@umich.edu
From: aaronz@vt.edu
From: aaronz@vt.edu
From: jzaremba@unicon.net
From: dlhaines@umich.edu
From: chmaurer@iupui.edu
From: zach.thomas@txstate.edu
From: dlhaines@umich.edu
>>> fhand = open('mbox.txt')
>>> for line in fhand:
	if not line.startswith('From:'):
		continue
	print(line)

	
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: zqian@umich.edu

From: gsilver@umich.edu

From: wagnermr@iupui.edu

From: zqian@umich.edu

From: antranig@caret.cam.ac.uk

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: ray@media.berkeley.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ray@media.berkeley.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: ray@media.berkeley.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: gopal.ramasammycook@gmail.com

From: gsilver@umich.edu

From: gsilver@umich.edu

From: stuart.freeman@et.gatech.edu

From: zqian@umich.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: zqian@umich.edu

From: wagnermr@iupui.edu

From: stuart.freeman@et.gatech.edu

From: tnguyen@iupui.edu

From: stuart.freeman@et.gatech.edu

From: wagnermr@iupui.edu

From: gopal.ramasammycook@gmail.com

From: ray@media.berkeley.edu

From: ray@media.berkeley.edu

From: zqian@umich.edu

From: wagnermr@iupui.edu

From: stuart.freeman@et.gatech.edu

From: chmaurer@iupui.edu

From: stuart.freeman@et.gatech.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: aaronz@vt.edu

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: wagnermr@iupui.edu

From: csev@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: rjlowe@iupui.edu

From: jimeng@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: gsilver@umich.edu

From: ian@caret.cam.ac.uk

From: csev@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: josrodri@iupui.edu

From: josrodri@iupui.edu

From: csev@umich.edu

From: ian@caret.cam.ac.uk

From: csev@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: knoop@umich.edu

From: knoop@umich.edu

From: knoop@umich.edu

From: knoop@umich.edu

From: knoop@umich.edu

From: cwen@iupui.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: csev@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: bkirschn@umich.edu

From: jimeng@umich.edu

From: ian@caret.cam.ac.uk

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: ian@caret.cam.ac.uk

From: jimeng@umich.edu

From: jimeng@umich.edu

From: ray@media.berkeley.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: stuart.freeman@et.gatech.edu

From: bkirschn@umich.edu

From: zqian@umich.edu

From: louis@media.berkeley.edu

From: dlhaines@umich.edu

From: bkirschn@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: bkirschn@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: bkirschn@umich.edu

From: bkirschn@umich.edu

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: stephen.marquard@uct.ac.za

From: david.horwitz@uct.ac.za

From: bkirschn@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: dlhaines@umich.edu

From: josrodri@iupui.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: hu2@iupui.edu

From: louis@media.berkeley.edu

From: bkirschn@umich.edu

From: josrodri@iupui.edu

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: josrodri@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: hu2@iupui.edu

From: cwen@iupui.edu

From: tnguyen@iupui.edu

From: sgithens@caret.cam.ac.uk

From: arwhyte@umich.edu

From: rjlowe@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: david.horwitz@uct.ac.za

From: josrodri@iupui.edu

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: david.horwitz@uct.ac.za

From: dlhaines@umich.edu

From: stephen.marquard@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: zqian@umich.edu

From: zqian@umich.edu

From: gbhatnag@umich.edu

From: dlhaines@umich.edu

From: jimeng@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ray@media.berkeley.edu

From: rjlowe@iupui.edu

From: jimeng@umich.edu

From: wagnermr@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: wagnermr@iupui.edu

From: cwen@iupui.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: stephen.marquard@uct.ac.za

From: gjthomas@iupui.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: jimeng@umich.edu

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: cwen@iupui.edu

From: gsilver@umich.edu

From: cwen@iupui.edu

From: stuart.freeman@et.gatech.edu

From: wagnermr@iupui.edu

From: stuart.freeman@et.gatech.edu

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: gsilver@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: tnguyen@iupui.edu

From: cwen@iupui.edu

From: bkirschn@umich.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: tnguyen@iupui.edu

From: cwen@iupui.edu

From: tnguyen@iupui.edu

From: cwen@iupui.edu

From: dlhaines@umich.edu

From: cwen@iupui.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ajpoland@iupui.edu

From: josrodri@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: dlhaines@umich.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gsilver@umich.edu

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: cwen@iupui.edu

From: lance@indiana.edu

From: lance@indiana.edu

From: dlhaines@umich.edu

From: lance@indiana.edu

From: chmaurer@iupui.edu

From: ian@caret.cam.ac.uk

From: lance@indiana.edu

From: lance@indiana.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ajpoland@iupui.edu

From: cwen@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: stephen.marquard@uct.ac.za

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: ian@caret.cam.ac.uk

From: rjlowe@iupui.edu

From: wagnermr@iupui.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: louis@media.berkeley.edu

From: ian@caret.cam.ac.uk

From: wagnermr@iupui.edu

From: wagnermr@iupui.edu

From: gsilver@umich.edu

From: wagnermr@iupui.edu

From: zqian@umich.edu

From: wagnermr@iupui.edu

From: stuart.freeman@et.gatech.edu

From: cwen@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: ssmail@indiana.edu

From: cwen@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: cwen@iupui.edu

From: wagnermr@iupui.edu

From: rjlowe@iupui.edu

From: dlhaines@umich.edu

From: jlrenfro@ucdavis.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: arwhyte@umich.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: nuno@ufp.pt

From: wagnermr@iupui.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: nuno@ufp.pt

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: cwen@iupui.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: rjlowe@iupui.edu

From: wagnermr@iupui.edu

From: gjthomas@iupui.edu

From: nuno@ufp.pt

From: wagnermr@iupui.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: zach.thomas@txstate.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: arwhyte@umich.edu

From: josrodri@iupui.edu

From: arwhyte@umich.edu

From: josrodri@iupui.edu

From: stephen.marquard@uct.ac.za

From: stephen.marquard@uct.ac.za

From: gjthomas@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: gjthomas@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: tnguyen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: mmmay@indiana.edu

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: cwen@iupui.edu

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: cwen@iupui.edu

From: bkirschn@umich.edu

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: cwen@iupui.edu

From: mmmay@indiana.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: lance@indiana.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: josrodri@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: david.horwitz@uct.ac.za

From: rjlowe@iupui.edu

From: sgithens@caret.cam.ac.uk

From: louis@media.berkeley.edu

From: louis@media.berkeley.edu

From: ktsao@stanford.edu

From: ray@media.berkeley.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: cwen@iupui.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: ostermmg@whitman.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: dlhaines@umich.edu

From: gopal.ramasammycook@gmail.com

From: jimeng@umich.edu

From: josrodri@iupui.edu

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: nuno@ufp.pt

From: wagnermr@iupui.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: gopal.ramasammycook@gmail.com

From: stuart.freeman@et.gatech.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: jimeng@umich.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: jimeng@umich.edu

From: zqian@umich.edu

From: cwen@iupui.edu

From: arwhyte@umich.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gjthomas@iupui.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: josrodri@iupui.edu

From: dlhaines@umich.edu

From: jimeng@umich.edu

From: dlhaines@umich.edu

From: jimeng@umich.edu

From: ray@media.berkeley.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: wagnermr@iupui.edu

From: cwen@iupui.edu

From: ssmail@indiana.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: josrodri@iupui.edu

From: sgithens@caret.cam.ac.uk

From: jimeng@umich.edu

From: jimeng@umich.edu

From: ktsao@stanford.edu

From: ray@media.berkeley.edu

From: ray@media.berkeley.edu

From: jimeng@umich.edu

From: louis@media.berkeley.edu

From: ktsao@stanford.edu

From: gbhatnag@umich.edu

From: ktsao@stanford.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gbhatnag@umich.edu

From: dlhaines@umich.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: josrodri@iupui.edu

From: josrodri@iupui.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: wagnermr@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: aaronz@vt.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: wagnermr@iupui.edu

From: gjthomas@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: aaronz@vt.edu

From: gjthomas@iupui.edu

From: zqian@umich.edu

From: josrodri@iupui.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: mmmay@indiana.edu

From: chmaurer@iupui.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: zqian@umich.edu

From: josrodri@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: ray@media.berkeley.edu

From: chmaurer@iupui.edu

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: rjlowe@iupui.edu

From: ian@caret.cam.ac.uk

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: aaronz@vt.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: chmaurer@iupui.edu

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: jimeng@umich.edu

From: chmaurer@iupui.edu

From: wagnermr@iupui.edu

From: josrodri@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: josrodri@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gopal.ramasammycook@gmail.com

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: ian@caret.cam.ac.uk

From: jimeng@umich.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: david.horwitz@uct.ac.za

From: gopal.ramasammycook@gmail.com

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gopal.ramasammycook@gmail.com

From: a.fish@lancaster.ac.uk

From: stuart.freeman@et.gatech.edu

From: stuart.freeman@et.gatech.edu

From: stuart.freeman@et.gatech.edu

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ian@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: david.horwitz@uct.ac.za

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gopal.ramasammycook@gmail.com

From: cwen@iupui.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: jimeng@umich.edu

From: mmmay@indiana.edu

From: jimeng@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: wagnermr@iupui.edu

From: mmmay@indiana.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: chmaurer@iupui.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: john.ellis@rsmart.com

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: stuart.freeman@et.gatech.edu

From: stuart.freeman@et.gatech.edu

From: zqian@umich.edu

From: jleasia@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: gopal.ramasammycook@gmail.com

From: dlhaines@umich.edu

From: sgithens@caret.cam.ac.uk

From: dlhaines@umich.edu

From: aaronz@vt.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: cwen@iupui.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: dlhaines@umich.edu

From: antranig@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: zach.thomas@txstate.edu

From: dlhaines@umich.edu

From: aaronz@vt.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: aaronz@vt.edu

From: ssmail@indiana.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ssmail@indiana.edu

From: zqian@umich.edu

From: stuart.freeman@et.gatech.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: stuart.freeman@et.gatech.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: cwen@iupui.edu

From: ian@caret.cam.ac.uk

From: dlhaines@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: gopal.ramasammycook@gmail.com

From: dlhaines@umich.edu

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: john.ellis@rsmart.com

From: john.ellis@rsmart.com

From: aaronz@vt.edu

From: cwen@iupui.edu

From: zqian@umich.edu

From: wagnermr@iupui.edu

From: aaronz@vt.edu

From: wagnermr@iupui.edu

From: gopal.ramasammycook@gmail.com

From: lance@indiana.edu

From: sgithens@caret.cam.ac.uk

From: ggolden@umich.edu

From: ggolden@umich.edu

From: cwen@iupui.edu

From: ggolden@umich.edu

From: ggolden@umich.edu

From: ggolden@umich.edu

From: ggolden@umich.edu

From: david.horwitz@uct.ac.za

From: antranig@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: antranig@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: david.horwitz@uct.ac.za

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: ian@caret.cam.ac.uk

From: gopal.ramasammycook@gmail.com

From: ian@caret.cam.ac.uk

From: david.horwitz@uct.ac.za

From: gopal.ramasammycook@gmail.com

From: antranig@caret.cam.ac.uk

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ray@media.berkeley.edu

From: ktsao@stanford.edu

From: sgithens@caret.cam.ac.uk

From: zqian@umich.edu

From: cwen@iupui.edu

From: antranig@caret.cam.ac.uk

From: zqian@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: antranig@caret.cam.ac.uk

From: antranig@caret.cam.ac.uk

From: ssmail@indiana.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: mmmay@indiana.edu

From: gopal.ramasammycook@gmail.com

From: aaronz@vt.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: ian@caret.cam.ac.uk

From: mmmay@indiana.edu

From: jimeng@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: lance@indiana.edu

From: sgithens@caret.cam.ac.uk

From: aaronz@vt.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: john.ellis@rsmart.com

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: ktsao@stanford.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: cwen@iupui.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: thoppaymallika@fhda.edu

From: chmaurer@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: chmaurer@iupui.edu

From: sgithens@caret.cam.ac.uk

From: chmaurer@iupui.edu

From: gsilver@umich.edu

From: zqian@umich.edu


From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: sgithens@caret.cam.ac.uk

From: david.horwitz@uct.ac.za

From: zqian@umich.edu

From: sgithens@caret.cam.ac.uk

From: ajpoland@iupui.edu

From: cwen@iupui.edu

From: gsilver@umich.edu

From: sgithens@caret.cam.ac.uk

From: jimeng@umich.edu

From: zqian@umich.edu

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: bkirschn@umich.edu

From: antranig@caret.cam.ac.uk

From: antranig@caret.cam.ac.uk

From: zqian@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: gopal.ramasammycook@gmail.com

From: zqian@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: john.ellis@rsmart.com

From: ajpoland@iupui.edu

From: chmaurer@iupui.edu

From: antranig@caret.cam.ac.uk

From: antranig@caret.cam.ac.uk

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: antranig@caret.cam.ac.uk

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: gopal.ramasammycook@gmail.com

From: zqian@umich.edu

From: kimsooil@bu.edu

From: kimsooil@bu.edu

From: kimsooil@bu.edu

From: zqian@umich.edu

From: ostermmg@whitman.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: zqian@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: jimeng@umich.edu

From: ray@media.berkeley.edu

From: ostermmg@whitman.edu

From: josrodri@iupui.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: rjlowe@iupui.edu

From: antranig@caret.cam.ac.uk

From: antranig@caret.cam.ac.uk

From: josrodri@iupui.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu

From: ian@caret.cam.ac.uk

From: antranig@caret.cam.ac.uk

From: zqian@umich.edu

From: wagnermr@iupui.edu

From: gsilver@umich.edu

From: gopal.ramasammycook@gmail.com

From: ajpoland@iupui.edu

From: wagnermr@iupui.edu

From: wagnermr@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ajpoland@iupui.edu

From: wagnermr@iupui.edu

From: wagnermr@iupui.edu

From: david.horwitz@uct.ac.za

From: ray@media.berkeley.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: ajpoland@iupui.edu

From: ostermmg@whitman.edu

From: cwen@iupui.edu

From: jimeng@umich.edu

From: josrodri@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: wagnermr@iupui.edu

From: hu2@iupui.edu

From: josrodri@iupui.edu

From: wagnermr@iupui.edu

From: rjlowe@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: ian@caret.cam.ac.uk

From: ajpoland@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: jimeng@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: rjlowe@iupui.edu

From: jimeng@umich.edu

From: sgithens@caret.cam.ac.uk

From: sgithens@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: ray@media.berkeley.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: cwen@iupui.edu

From: bkirschn@umich.edu

From: gsilver@umich.edu

From: john.ellis@rsmart.com

From: aaronz@vt.edu

From: bkirschn@umich.edu

From: gopal.ramasammycook@gmail.com

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: ajpoland@iupui.edu

From: aaronz@vt.edu

From: sgithens@caret.cam.ac.uk

From: aaronz@vt.edu

From: jimeng@umich.edu

From: ostermmg@whitman.edu

From: ostermmg@whitman.edu

From: jimeng@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: sgithens@caret.cam.ac.uk

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: gopal.ramasammycook@gmail.com

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: dlhaines@umich.edu

From: wagnermr@iupui.edu


From: aaronz@vt.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: wagnermr@iupui.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: kimsooil@bu.edu

From: kimsooil@bu.edu

From: aaronz@vt.edu

From: nuno@ufp.pt

From: arwhyte@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: ajpoland@iupui.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ajpoland@iupui.edu

From: wagnermr@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: sgithens@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: josrodri@iupui.edu

From: josrodri@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: josrodri@iupui.edu

From: zqian@umich.edu

From: arwhyte@umich.edu

From: rjlowe@iupui.edu

From: dlhaines@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: arwhyte@umich.edu

From: wagnermr@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: josrodri@iupui.edu

From: gjthomas@iupui.edu


From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: sgithens@caret.cam.ac.uk

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: ray@media.berkeley.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: david.horwitz@uct.ac.za

From: antranig@caret.cam.ac.uk

From: ggolden@umich.edu

From: antranig@caret.cam.ac.uk

From: ggolden@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu


From: david.horwitz@uct.ac.za

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: wagnermr@iupui.edu

From: rjlowe@iupui.edu

From: gopal.ramasammycook@gmail.com

From: david.horwitz@uct.ac.za

From: zqian@umich.edu

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: ray@media.berkeley.edu

From: hu2@iupui.edu

From: mmmay@indiana.edu

From: bkirschn@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: ray@media.berkeley.edu

From: ray@media.berkeley.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: csev@umich.edu

From: josrodri@iupui.edu

From: csev@umich.edu

From: zqian@umich.edu

From: bahollad@indiana.edu

From: aaronz@vt.edu

From: jzaremba@unicon.net

From: ajpoland@iupui.edu

From: aaronz@vt.edu

From: csev@umich.edu

From: rjlowe@iupui.edu

From: nuno@ufp.pt

From: nuno@ufp.pt

From: mmmay@indiana.edu

From: bkirschn@umich.edu

From: jimeng@umich.edu

From: bkirschn@umich.edu

From: bkirschn@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: john.ellis@rsmart.com

From: zqian@umich.edu

From: jzaremba@unicon.net

From: jimeng@umich.edu

From: bkirschn@umich.edu

From: bkirschn@umich.edu

From: bkirschn@umich.edu

From: bkirschn@umich.edu

From: zqian@umich.edu

From: ktsao@stanford.edu

From: mmmay@indiana.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: dlhaines@umich.edu

From: bkirschn@umich.edu

From: zqian@umich.edu

From: bkirschn@umich.edu

From: ray@media.berkeley.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: zach.thomas@txstate.edu

From: ostermmg@whitman.edu

From: bkirschn@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: wagnermr@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: zach.thomas@txstate.edu

From: wagnermr@iupui.edu

From: gsilver@umich.edu

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: hu2@iupui.edu

From: ajpoland@iupui.edu

From: wagnermr@iupui.edu

From: david.horwitz@uct.ac.za

From: zqian@umich.edu

From: jzaremba@unicon.net

From: cwen@iupui.edu

From: ktsao@stanford.edu

From: bahollad@indiana.edu

From: zach.thomas@txstate.edu

From: cwen@iupui.edu

From: ajpoland@iupui.edu

From: wagnermr@iupui.edu

From: wagnermr@iupui.edu

From: aaronz@vt.edu

From: sgithens@caret.cam.ac.uk

From: a.fish@lancaster.ac.uk

From: aaronz@vt.edu

From: david.horwitz@uct.ac.za

From: david.horwitz@uct.ac.za

From: zqian@umich.edu

From: jzaremba@unicon.net

From: zach.thomas@txstate.edu

From: jzaremba@unicon.net

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: john.ellis@rsmart.com

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: chmaurer@iupui.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: kimsooil@bu.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: kimsooil@bu.edu

From: nuno@ufp.pt

From: kimsooil@bu.edu

From: ajpoland@iupui.edu

From: chmaurer@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: ajpoland@iupui.edu

From: dlhaines@umich.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: wagnermr@iupui.edu

From: david.horwitz@uct.ac.za

From: jleasia@umich.edu

From: david.horwitz@uct.ac.za

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: cwen@iupui.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: kimsooil@bu.edu

From: mmmay@indiana.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: mmmay@indiana.edu

From: kimsooil@bu.edu

From: aaronz@vt.edu

From: dlhaines@umich.edu

From: zqian@umich.edu

From: mmmay@indiana.edu

From: dlhaines@umich.edu

From: cwen@iupui.edu

From: kimsooil@bu.edu

From: kimsooil@bu.edu

From: kimsooil@bu.edu

From: hu2@iupui.edu

From: zqian@umich.edu

From: kimsooil@bu.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: rjlowe@iupui.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: hu2@iupui.edu

From: dlhaines@umich.edu

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: gsilver@umich.edu

From: mbreuker@loi.nl

From: mbreuker@loi.nl

From: mbreuker@loi.nl

From: mbreuker@loi.nl

From: mbreuker@loi.nl

From: mbreuker@loi.nl

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: a.fish@lancaster.ac.uk

From: dlhaines@umich.edu

From: mbreuker@loi.nl

From: david.horwitz@uct.ac.za

From: zach.thomas@txstate.edu

From: jimeng@umich.edu

From: zqian@umich.edu

From: jzaremba@unicon.net

From: colin.clark@utoronto.ca

From: ray@media.berkeley.edu

From: ray@media.berkeley.edu

From: ray@media.berkeley.edu

From: ray@media.berkeley.edu

From: louis@media.berkeley.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: ajpoland@iupui.edu

From: wagnermr@iupui.edu

From: zqian@umich.edu

From: ktsao@stanford.edu

From: ray@media.berkeley.edu

From: aaronz@vt.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: bahollad@indiana.edu

From: aaronz@vt.edu

From: zqian@umich.edu

From: ray@media.berkeley.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: bahollad@indiana.edu

From: ray@media.berkeley.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: ray@media.berkeley.edu

From: jzaremba@unicon.net

From: louis@media.berkeley.edu

From: rjlowe@iupui.edu

From: ajpoland@iupui.edu

From: ray@media.berkeley.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: ray@media.berkeley.edu

From: zqian@umich.edu

From: bkirschn@umich.edu

From: mbreuker@loi.nl

From: zqian@umich.edu

From: gsilver@umich.edu

From: louis@media.berkeley.edu

From: bkirschn@umich.edu

From: bkirschn@umich.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: zach.thomas@txstate.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ray@media.berkeley.edu

From: ktsao@stanford.edu

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: chmaurer@iupui.edu

From: ian@caret.cam.ac.uk

From: gjthomas@iupui.edu

From: gjthomas@iupui.edu

From: aaronz@vt.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: mbreuker@loi.nl

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: dlhaines@umich.edu

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: chmaurer@iupui.edu

From: chmaurer@iupui.edu

From: zqian@umich.edu

From: gjthomas@iupui.edu

From: gsilver@umich.edu

From: ian@caret.cam.ac.uk

From: ajpoland@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: zach.thomas@txstate.edu

From: ajpoland@iupui.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: gjthomas@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: dlhaines@umich.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: cwen@iupui.edu

From: ktsao@stanford.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: gsilver@umich.edu

From: gsilver@umich.edu

From: zqian@umich.edu

From: jzaremba@unicon.net

From: aaronz@vt.edu

From: aaronz@vt.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: dlhaines@umich.edu

From: ajpoland@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: rjlowe@iupui.edu

From: dlhaines@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ian@caret.cam.ac.uk

From: aaronz@vt.edu

From: aaronz@vt.edu

From: ktsao@stanford.edu

From: ian@caret.cam.ac.uk

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: zqian@umich.edu

From: aaronz@vt.edu

From: aaronz@vt.edu

From: jzaremba@unicon.net

From: dlhaines@umich.edu

From: chmaurer@iupui.edu

From: zach.thomas@txstate.edu

From: dlhaines@umich.edu

>>> From: chmaurer@iupui.edu

From: ajpoland@iupui.edu

SyntaxError: multiple statements found while compiling a single statement
>>> fhand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fhand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> fhand = open('mbox.txt')
>>> for line in fhand:
	line = line.rstrip()
	if line.find('@uct.ac.za') == -1: continue
        print(line)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> for line in fhand:
	line = line.rstrip()
	if line.find('@uct.ac.za') == -1: continue
	print(line)

	
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r39753 | david.horwitz@uct.ac.za | 2008-01-04 13:05:51 +0200 (Fri, 04 Jan 2008) | 1 line
From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
r35793 | david.horwitz@uct.ac.za | 2007-09-26 05:26:53 -0400 (Wed, 26 Sep 2007) | 2 lines
r38153 | david.horwitz@uct.ac.za | 2007-11-14 01:53:07 -0500 (Wed, 14 Nov 2007) | 1 line
r39548 | david.horwitz@uct.ac.za | 2007-12-20 10:00:05 -0500 (Thu, 20 Dec 2007) | 1 line
From david.horwitz@uct.ac.za Wed Jan  2 09:54:32 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 09:40:42 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 09:38:43 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 09:16:03 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 09:07:48 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 08:55:03 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 08:37:45 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 08:23:44 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 08:17:41 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 05:16:10 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 04:40:56 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 04:24:50 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 03:56:59 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 03:22:37 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 03:04:19 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 03:02:55 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Jan  2 02:53:22 2008
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Mon Dec 24 03:06:42 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From stephen.marquard@uct.ac.za Mon Dec 24 02:06:31 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 09:54:17 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za

From david.horwitz@uct.ac.za Fri Dec 21 09:50:38 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 09:44:11 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r39593 | david.horwitz@uct.ac.za | 2007-12-21 16:08:28 +0200 (Fri, 21 Dec 2007) | 3 lines
From david.horwitz@uct.ac.za Fri Dec 21 09:33:55 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 09:09:23 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Fri Dec 21 09:08:22 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 09:03:52 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 06:30:05 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 06:17:07 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r39578 | david.horwitz@uct.ac.za | 2007-12-21 10:30:23 +0200 (Fri, 21 Dec 2007) | 1 line
From david.horwitz@uct.ac.za Fri Dec 21 06:12:21 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r39577 | david.horwitz@uct.ac.za | 2007-12-21 10:19:00 +0200 (Fri, 21 Dec 2007) | 1 line
From david.horwitz@uct.ac.za Fri Dec 21 06:05:26 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 06:01:02 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 04:29:36 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 04:24:25 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 03:31:56 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Fri Dec 21 03:20:08 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec 20 10:01:26 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec 20 07:59:57 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f 
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Thu Dec 20 06:43:49 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec 20 05:49:17 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec 20 05:39:52 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Thu Dec 20 04:22:43 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From stephen.marquard@uct.ac.za Thu Dec 20 04:19:28 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec 20 04:13:41 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec 20 03:59:12 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From stephen.marquard@uct.ac.za Wed Dec 19 13:31:20 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za
From stephen.marquard@uct.ac.za Wed Dec 19 03:40:33 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za


From stephen.marquard@uct.ac.za Wed Dec 19 03:20:57 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f



From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Wed Dec 19 03:08:44 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Wed Dec 19 02:55:09 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Wed Dec 19 02:40:51 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 09:08:11 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 07:49:52 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 07:49:28 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 07:49:19 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 07:49:06 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 07:47:38 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 06:56:24 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 06:55:54 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 06:51:56 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za
Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 06:50:02 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 06:33:34 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Tue Dec 18 06:32:11 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za
From stephen.marquard@uct.ac.za Tue Dec 18 06:31:24 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f


From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za
From stephen.marquard@uct.ac.za Sun Dec 16 03:59:13 2007


X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From stephen.marquard@uct.ac.za Sun Dec 16 03:57:28 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f

From: stephen.marquard@uct.ac.za

Author: stephen.marquard@uct.ac.za

From david.horwitz@uct.ac.za Fri Dec 14 03:31:09 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f


From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za

#38981  	Thu Dec 06 03:19:40 MST 2007  	david.horwitz@uct.ac.za  	 SAK-12324 Modifications to site-manage

#39019  	Fri Dec 07 00:55:01 MST 2007  	david.horwitz@uct.ac.za  	 SAK-12324 Modify site


#39020  	Fri Dec 07 02:53:25 MST 2007  	david.horwitz@uct.ac.za  	 SAK-12324 add the course site logic to allowAddCourseSite(id)

r38948 | david.horwitz@uct.ac.za | 2007-12-03 10:18:02 -0500 (Mon, 03 Dec 2007) | 1 line


#34436	Mon Aug 27 03:41:14 MST 2007	david.horwitz@uct.ac.za	SAK-11282 check content suitablity before submitting

From david.horwitz@uct.ac.za Fri Dec  7 05:01:19 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f



From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za

From david.horwitz@uct.ac.za Fri Dec  7 03:28:37 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f


From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za

From david.horwitz@uct.ac.za Thu Dec  6 05:27:28 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f


From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Thu Dec  6 03:57:03 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f


From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Mon Dec  3 10:25:25 2007

X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f


From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za

From david.horwitz@uct.ac.za Fri Nov 30 10:21:12 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r38522 | david.horwitz@uct.ac.za | 2007-11-21 05:14:25 -0500 (Wed, 21 Nov 2007) | 1 line
r38523 | david.horwitz@uct.ac.za | 2007-11-21 05:41:48 -0500 (Wed, 21 Nov 2007) | 1 line
From david.horwitz@uct.ac.za Fri Nov 23 04:27:02 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Nov 21 11:26:30 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Nov 21 05:48:24 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r38114 | david.horwitz@uct.ac.za | 2007-11-12 04:17:19 -0500 (Mon, 12 Nov 2007) | 1 line

r38115 | david.horwitz@uct.ac.za | 2007-11-12 04:36:57 -0500 (Mon, 12 Nov 2007) | 1 line
r38116 | david.horwitz@uct.ac.za | 2007-11-12 04:39:21 -0500 (Mon, 12 Nov 2007) | 1 line
r38114 | david.horwitz@uct.ac.za | 2007-11-12 04:17:19 -0500 (Mon, 12 Nov 2007) | 1 line
r38117 | david.horwitz@uct.ac.za | 2007-11-12 04:53:08 -0500 (Mon, 12 Nov 2007) | 1 line
r38259 | david.horwitz@uct.ac.za | 2007-11-18 02:35:09 -0500 (Sun, 18 Nov 2007) | 1 line

r38153 | david.horwitz@uct.ac.za | 2007-11-14 01:53:07 -0500 (Wed, 14 Nov 2007) | 1 line
From david.horwitz@uct.ac.za Sun Nov 18 02:41:27 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Nov 14 01:58:47 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Mon Nov 12 04:58:44 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Mon Nov 12 04:44:46 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Mon Nov 12 04:42:30 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za

Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Mon Nov 12 04:22:56 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za

r37784 | david.horwitz@uct.ac.za | 2007-11-06 11:11:51 -0500 (Tue, 06 Nov 2007) | 1 line
From david.horwitz@uct.ac.za Tue Nov  6 11:47:55 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f

From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Tue Nov  6 11:16:42 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Tue Nov  6 04:20:19 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r37660 | david.horwitz@uct.ac.za | 2007-10-31 04:16:00 -0400 (Wed, 31 Oct 2007) | 1 line
From david.horwitz@uct.ac.za Thu Nov  1 03:45:50 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Oct 31 04:50:54 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Wed Oct 31 04:19:43 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
r37532 | david.horwitz@uct.ac.za | 2007-10-30 05:35:42 -0400 (Tue, 30 Oct 2007) | 1 line
From david.horwitz@uct.ac.za Tue Oct 30 07:48:17 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Tue Oct 30 05:40:21 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
From david.horwitz@uct.ac.za Mon Oct 29 06:46:00 2007
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
From: david.horwitz@uct.ac.za
Author: david.horwitz@uct.ac.za
>>> fname = input('Enter the file name:')
Enter the file name:Warlord
>>> fhand = open(fname)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fhand = open(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'Warlord'
>>> fname = input('Enter the file name:')
Enter the file name:mbox
>>> fhand = open(fname)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    fhand = open(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'mbox'
>>> fname = input('Enter the file name:')
Enter the file name:warlord.txt
>>> fhand = open(fname)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fhand = open(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'warlord.txt'
>>> fname = input('Enter the file name:')
Enter the file name:mbox.txt
>>> fhand = open(fname)
>>> for line in fhand:
	if line.startswith('Subject:')
	
SyntaxError: invalid syntax
>>> for line in fhand:
	if line.startswith('Subject:'):
		count = count+1

		
Traceback (most recent call last):
  File "<pyshell#32>", line 3, in <module>
    count = count+1
NameError: name 'count' is not defined
>>> count = 0
>>> for line in fhand:
	if line.startswith('Subject:'):
		count = count+1

		
>>> print('There were', count, 'subject lines in', fname)
There were 1796 subject lines in mbox.txt
>>> fname = input('Enter the file name:')
Enter the file name:mbox.txt
>>> try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()

	
>>> count = 0
>>> for line in fhand:
	if line.startswith('Subject:'):
		count = count+1

		
>>> print('There were', count, 'subject lines in', fname)
There were 1797 subject lines in mbox.txt
>>> fout = open('output.txt', 'w')
>>> print(fout)
<_io.TextIOWrapper name='output.txt' mode='w' encoding='cp936'>
>>> line1 = "This here's the wattle,\n"
>>> fout.write(line1)
24
>>> line2 = 'the emblem of our land.\n'
>>> fout.write(line2)
24
>>> fout.close()
>>> s = '1 2\t 3\n 4'
>>> print(s)
1 2	 3
 4
>>> s
'1 2\t 3\n 4'
>>> print(repr(s))
'1 2\t 3\n 4'
>>> 
