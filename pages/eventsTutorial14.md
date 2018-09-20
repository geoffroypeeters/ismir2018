title: Tutorials
author: peeters
slug: events-tutorial-14
category:
tags: eventsTutorial14
order: 1
parent: events

## Open Source and Reproducible MIR Research

**Speakers: Brian McFee, Thor Kell**

**Abstract:** The goal of this tutorial is to provide hands-on, practical training for MIR researchers to learn modern tools for improving the quality of their research software.

We will provide a project template repository, which we will use as scaffolding to demonstrate practices and techniques inlcuding version control, continuous integration, automatic documentation, environments & software dependency tracking, and packaging & distribution.  While many of the techniques we will cover are independent of language or programming environment, the practices are best demonstrated by example, and we expect Python to be the most accessible and generally useful language for the expected attendees.

The tutorial will begin with a brief introduction to version control with git and GitHub.  We will only cover the basics: creating an account, cloning, pushing, and pulling.  We will walk attendees through the process of making their own copy of the repository, verifying that tests and documentation work, implementing some simple functionality, and working with automatic testing. The goal of this exercise is to expose attendees to modern development practices, so that their software is continuously tested during development.  Attendees will then learn how to create documentation with Sphinx and automate the process with the ReadTheDocs service. We will teach standard documentation style, and provide an exercise in which attendees write documentation for a previously undocumented function. We will also discuss how to write README files and how to make a package easy for others to use.
We note that many of the tools we will demonstrate are provided by web services (Travis, GitHub, etc.), which have freely available counterparts that can run on local servers (Jenkins, 8 GitLab, 9 etc.). We will provide pointers to these alternative implementations, but for ease of exposition and simplicity, we will stick to the web-based services for the tutorial.

Finally, we will close with a tour of the Python/MIR ecosystem. This part of the tutorial will give an overview of the available packages commonly used in MIR research, such as the scipy stack, pandas, librosa, mir eval, and jupyter. We will spend some extra time on Jupyter, including plotting and sonification, as well as discussing how to save and iterate on notebooks.

<TABLE>

<TR>
<TD>
<img src="../images/tutorial/tutorial_photo_mcfee.jpg">
</TD>
<TD>
Brian McFee is a Moore-Sloan Fellow at New York University's Center for Data Science and Music and Audio Research Lab (MARL). He received the B.S. degree (2003) in Computer Science from the University of California, Santa Cruz, and M.S. (2008) and Ph.D. (2012) degrees in Computer Science and Engineering from the University of California, San Diego. His work touches on various topics at the intersection of machine learning, information retrieval, and audio analysis. He is an active open source software developer, and the principal maintainer of the librosa package for music and audio signal processing. His favorite genre is "chip-tune", and he likes dogs.
</TD>
</TR>


<TR>
<TD>
<img src="../images/tutorial/tutorial_photo_kell.jpg">
</TD>
<TD>
Thor Kell earned his B.Sc in Computer Science & Music from the University of Victoria in 2011, and an M.A. in Music Technology from McGill in 2015. He has worked for SoundCloud, The Echo Nest, and is currently an engineer at Spotify. His interests include algorithmic music creation as well as track ordering and automatic mixing for DJ sets. His favorite genre is ”post”, and he likes cats.
</TD>
</TR>

</TABLE>
