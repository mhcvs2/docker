

<pre>
<code>
1. pip download twitter.common.quantity -d /var/www/html/pypi/sample

2. find . -name requirements.txt -exec cat {} \;> pip_requirement.all

#!/bin/bash

PIP_REQUIRE="pip_requirement.all"

while read LINE
do
  if [[ $LINE =~ ^[a-zA-Z] ]]
  then
    echo $LINE
    pip download $LINE -d /var/www/html/pypi/sample  #仅下载不安装
  fi
done < $PIP_REQUIRE


-----------------------------------------
httpd.conf 中
DocumentRoot 下的 Directory

Options Indexes FollowSymLinks
Require all granted

不能有index.html
镜像的配置满足
------------------------------------------


docker run -d --name=pip -p8888:80 -v/var/www/html:/usr/local/apache2/htdocs registry.bst-1.cns.bstjpc.com:5000/httpd:2.4
</code>
</pre>