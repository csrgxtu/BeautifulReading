
default:	build

clean:
	rm -rf Makefile objs

build:
	$(MAKE) -f objs/Makefile
	$(MAKE) -f objs/Makefile manpage

install:
	$(MAKE) -f objs/Makefile install

upgrade:
	/Users/archer/Documents/BeautifulReading/bin/openresty/nginx/sbin/nginx -t

	kill -USR2 `cat /Users/archer/Documents/BeautifulReading/bin/openresty/nginx/logs/nginx.pid`
	sleep 1
	test -f /Users/archer/Documents/BeautifulReading/bin/openresty/nginx/logs/nginx.pid.oldbin

	kill -QUIT `cat /Users/archer/Documents/BeautifulReading/bin/openresty/nginx/logs/nginx.pid.oldbin`
