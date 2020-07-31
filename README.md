**Cookie Breaker**

A python script to extract and analyze response\'s cookies.

-   Missing HttpOnly Flag on Session Cookies - If a program that braces
    HttpOnly observes a Cookie containing the HttpOnly banner, and
    client side substance code endeavors to explore the Cookie, the
    program reestablishes an unfilled string as the result. This makes
    the catch flop by forestalling the poisonous (generally XSS) code
    from sending the data to an assailant\'s site.

-   Missing Secure Flag on Session Cookies - The ensured standard is an
    elective that can be set by the application server when sending
    another Cookie to the customer inside a HTTP Response. The
    explanation behind the shielded banner is to shield Cookies from
    being seen by unapproved parties due to the transmission of a the
    Cookie in clear substance.

-   Domain of Session Cookie isn\'t set fittingly - The \'locale\'
    trademark infers the space for which the Cookie is valid and can be
    submitted with each arrangement for this space or its subdomains. If
    this trademark isn\'t showed up, by then the hostname of the
    starting server is used as the default regard.

-   Path Attribute on Session Cookie set to root - The Path request of a
    Cookie picks the URL route for which the Cookie will be broad. For
    example, consider the space report.com. The application to be
    attempted are report.com/r1 and report.com/r2 where /r1 and /r2 are
    separated applications on the space report.com exclusively. If the
    get-together tcookie has been disclosed to interweave the sales
    path=/for the application report.com/r1 or report.com/r2, by then
    this cookie will be authentic for all application ways, from the
    root stock downwards on the web server.
    
   
![](.//media/image1.png)

![](.//media/image2.png)

References:
LucideusTech,
Python Programming,
PortSwigger,
Request-Response

Thank You.
