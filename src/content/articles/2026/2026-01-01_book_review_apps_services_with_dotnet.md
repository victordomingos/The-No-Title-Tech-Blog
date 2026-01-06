Title: Book review — Apps and Services with .Net 8 (2nd Edition), by Mark J. Price
Date: 2026-01-01 23:00
Lang: en
Tags: dotnet, .NET, csharp, C#, apps, services, Azure, ASP.NET Core, Entity Framework, books, Mark J. Price, learning, libraries
Category: Book Reviews
Slug: book-review-apps-services-dotnet-8
Author: Victor Domingos
Cover: images/2026/apps_services_dotnet_cover.jpg
Summary: For a long time, I have been writing here about Python, Python projects, and Python books. It was one of my first programming languages, and the first one I fell in love with. So much so that I have used it as my go-to option for personal side projects, quick prototyping, and algorithm study. However, my professional life as a software developer has been based mostly on C# and .NET. At first, it felt like an overly verbose version of Python; over time, though, it became progressively more natural to me—so much so that I no longer prefer one over the other.

As part of my journey, I felt the need to deepen my knowledge of C# and .NET. Over the years, I read several good and interesting books which, unfortunately, I did not review here. Apps and Services with .NET came at a moment when books focused mainly on introducing language features were starting to feel limiting and repetitive. I bought this book because I wanted something that could help fill a few gaps and update the knowledge I had gained through formal training and professional experience in legacy .NET Framework projects, in order to better prepare myself for modern .NET.

![Python Distilled]({static}/images/2026/apps_services_dotnet_ch06.jpg)

When I received the package in the mail, I was surprised by the weight and thickness of the book—it has nearly 800 pages. I decided to take it one chapter at a time, sequentially, and it turned out to be a good way to approach it.

That said, since each chapter is largely independent, I found myself skipping ahead at certain points to read chapters that interested me more, such as those covering multitasking and async/await, third-party libraries, or fault tolerance with Polly. By doing so — and then returning to where I had left off — I discovered two or three important tips that I could immediately apply to projects I had been involved in. In that sense, it is also a book that can be read in a non-linear way.

This book is best suited for junior to mid-level developers, as well as for more experienced developers transitioning from legacy .NET Framework projects to modern .NET.

I like the fact that the book includes a large number of code samples covering almost everything it discusses, which you can download and experiment with. After all, the best learning happens when you do not just read about something, but actually try it and use it.

What I do not like is that the code samples in the printed book are shown in greyscale. It feels like reading a C or C++ book from 20 or 30 years ago. The good news is that the PDF version includes proper coloured syntax highlighting, as well as coloured figures, which makes it much easier to follow along. For that reason, you really should not limit yourself to the paper version.

### Book structure and contents

According to the preface, after an introductory first chapter, the book is organized around four general themes: Data, Libraries, Services, and Apps.

Each chapter begins with a nice and easy to read introduction section. At the end of each  chapter you will find with some topics for practice and further exploration, including some questions, links for more information or exercise suggestions. oh, and a summary, of course! :-)

#### Data

So, under the first theme, the opening three chapters cover SQL Server and ADO.NET, Entity Framework Core, and NoSQL databases using Azure Cosmos DB.

#### Libraries

The second group covers a number of useful first- and third-party libraries. As such, it will be particularly valuable for readers who are already familiar with C# and its common usage with databases, and who are starting to encounter performance issues and other typical developer pains. Chapter 5 focuses on multitasking and concurrency, and serves as a good introduction to performance improvements that can be applied once proper algorithmic refinement is in place.

In Chapter 6, the author introduces several popular and useful third-party libraries, such as ImageSharp (image manipulation), Humanizer (text and number formatting), Serilog (structured logging), AutoMapper (object-to-object mapping), FluentAssertions (testing with a more natural, fluent syntax), FluentValidation (strongly typed validation rules), and QuestPDF (PDF document generation).

Chapter 7 addresses the handling of dates, times, and internationalization. Date and time handling is particularly challenging in international or global projects, where user bases span multiple time zones, daylight saving changes, and other complexities. For more advanced date and time manipulation, the Noda Time third-party library is introduced. The chapter also covers language resources for user interface localization.

#### Services

n Chapter 8, the book introduces ASP.NET Core Minimal APIs, a way to build web services and APIs with reduced boilerplate, introduced in .NET 6. It explains route and parameter mapping, API documentation and testing with [Swagger](https://swagger.io){:target=_blank}, as well as testing using Visual Studio Code (via the REST Client extension) and Visual Studio 2022 (with .http files and the Endpoints Explorer). The chapter also includes a brief discussion on CORS (Cross-Origin Resource Sharing) and on building a simple client for the API. This chapter works well as an introduction and a starting point for further study using more in-depth, specialized books.

Chapter 9 revisits some fundamentals that directly affect application and service performance and resiliency, and explores ways to improve them. It discusses common performance bottlenecks, in-memory and distributed caching techniques, fault tolerance with [Polly](https://www.pollydocs.org){:target=_blank}, queueing with [RabbitMQ](https://www.rabbitmq.com){:target=_blank}, and the implementation of long-running background services, including a section on the open-source background job manager [Hangfire](https://www.hangfire.io){:target=_blank}. I must confess this was one of my favourite chapters, as some of the tips proved immediately useful for tasks I was about to tackle in a project I was working on at the time.

Chapters 10 to 13 focus respectively on Azure Functions, SignalR, GraphQL, and gRPC. These technologies are part of the broader .NET ecosystem and are widely used across modern platforms, from serverless backends and real-time web applications to API-driven and microservices-based systems. For this reason, it is useful to be familiar with them, even if they are not part of one’s daily toolbox. Many third-party frameworks built on C# and .NET — such as [DevExpress XAF Blazor](https://www.devexpress.com/products/net/application_framework/){:target=_blank}, ASP.NET Core–based platforms, or GraphQL servers like [Hot Chocolate](https://chillicream.com/docs/hotchocolate/v15){:target=_blank} — rely on or integrate some of these technologies, often behind the scenes.


#### Apps

he final group of chapters, from Chapter 14 to Chapter 16, covers three types of user interfaces that can be built with .NET, starting with ASP.NET Core MVC, followed by web components based on Blazor, and finally desktop and mobile applications using .NET MAUI.

These chapters effectively close the book’s cycle, in the sense that by this point the reader will have been introduced to a broad set of tools for managing data storage, processing, and user interfaces, both locally and in the cloud.

### Conclusions

This book fits nicely at a specific point in a .NET developer’s learning journey: when the fundamentals of the programming language, along with basic data structures and algorithms, have already been acquired, but there are still many gaps to fill and limited real-world experience. It can also be useful as a way to refresh knowledge acquired when working with earlier versions of the .NET Framework and its ecosystem. That said, it does not offer much guidance on software architecture or other more advanced topics. As a result, for senior and more experienced engineers, it may feel somewhat superficial and unlikely to provide significant professional growth.

Depending on your background and day-to-day work, some chapters may fall more into the category of _nice to know_ rather than immediately useful. As is often the case, however, you never really know what you will need for your next project or your next job, so there is still value in being exposed to those topics.

Overall, _Apps and Services with .NET_ is a solid, practical book for developers who already know C# and want a broader, hands-on understanding of the modern .NET ecosystem.

As a practical note, it is worth mentioning that if you choose to purchase the printed version of the book, the publisher also provides a free PDF download. This is particularly convenient when reading away from the rather voluminous paperback edition.

Finally, it is worth keeping in mind that the author is already preparing [another similar book focused on .NET 10](https://www.packtpub.com/en-us/product/apps-and-services-with-net-10-9781835469026){:target=_blank}, the latest LTS version, which was released by Microsoft less than two months ago. This new book, scheduled for release later this year, will certainly include more up-to-date content and may therefore be a better choice for some readers. According to the publisher’s notes, it will include at least two interesting new chapters, such as Building Desktop Apps Using Avalonia and Building an LLM-Based Chat Service. That said, the current book may still be worth picking up at a discount, as many of its chapters remain relevant today—and, after all, .NET 8 will be around for quite some time.

_______

### Get the book:

- [www.packtpub.com/en-us/product/apps-and-services-with-net-8-9781837637133](https://www.packtpub.com/en-us/product/apps-and-services-with-net-8-9781837637133){:target=_blank}

- [www.amazon.com/-/pt/dp/183763713X](https://www.amazon.com/-/pt/dp/183763713X){:target=_blank}  
 

<hr ><small>
<strong>Disclosure Notice:  </strong>
For this review, I bought myself a copy of the book, paying as a regular costumer. I do not personally know the author, nor did I receive any form of compensation. The link to the publisher and the Amazon book store are provided as reference only, I am not making any profit from it.
</small>

