title: Tutorials
author: peeters
slug: events-tutorial-01
category:
tags: eventsTutorial01
order: 1
parent: events

## Music Separation with DNNs: Making It Work

**Speakers: Antoine Liutkus, Fabian-Robert Stöter**

**Abstract:** This tutorial concerns music source separation, that we also call music demixing, with a resolute focus on methods using DNN. 

* In an introductory part, we will motivate the tutorial by explaining how music separation with DNN emerged with data-driven methods coming from machine-learning or image processing communities. This comes with machine-learning tricks to make methods work in practice. Meanwhile, many audio processing good practices are often forgotten or not correctly applied, although they are mandatory for good performance.

* In a second part, we present and discuss the few concepts that are mandatory to design a source separation method. Each point will firstly be the focus of screencasting from an interactive notebook session that all the audience will be invited to, and then will also be explained with a theoretical presentation when appropriate. The whole tutorial will be thus split into practical hands-on sessions using online interactive Python sessions and more classical theoretical insights.

* The third part of the tutorial provides some feedback on what seems to be important to get good performance in practice, with a focus on the training stage. On the one hand, many of the tricks discussed there are not often discussed in papers because a lot of them are negative results that are hard to publish: some interesting ideas that turn out ineffective yet. On the other hand, we also show how some very simple things make a huge difference in practice.

* In the following part, we pick one single system, resulting from the previous discussion, and show how its performance can be dramatically improved by using just a few simple tricks at test time, including resynthesis methods, filtering tricks, and how to go stereo.

This tutorial is first targetted at PhD students and at engineers, that want to implement audio demixing methods in practice and to achieve state of the art performance while keeping highly readable code. Second, by showing how pytorch enables easy design and debugging, including new cost functions, architectures, etc., it will hopefully be of interest to researchers wondering how to do actual investigations on audio with DNNs, without being just users of high-level black-box systems.

<TABLE>

<TR>
<TD>
<img src="../images/tutorial_photo_liutkus.jpg">
</TD>
<TD>
Antoine Liutkus received the State Engineering degree from Télécom ParisTech, France, in 2005, and the M.Sc. degree in acoustics, computer science and signal processing applied to music (ATIAM) from the Université Pierre et Marie Curie (Paris VI), Paris, in 2005. He worked as a research engineer on source separation at Audionamix from 2007 to 2010 and obtained his PhD in electrical engineering at Télécom ParisTech in 2012. He is currently researcher at Inria, France. His research interests include audio source separation and machine learning.
</TD>
</TR>

<TR>
<TD>
<img src="../images/tutorial_photo_stoter.jpg">
</TD>
<TD>
Fabian-Robert Stöter received the diploma degree in electrical engineering in 2012 from the Leibniz Universität Hannover and worked towards his Ph.D. degree in audio signal processing in the research group of B. Edler at the International Audio Laboratories Erlangen, Germany. He is currently researcher at Inria, France. His research interests include supervised and unsupervised methods for audio source separation and signal analysis of highly overlapped sources.
</TD>
</TR>

</TABLE>



