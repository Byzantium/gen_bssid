CC= gcc
CPPFLAGS=
CFLAGS= -O2 -Wall -Werror -g
LDFLAGS=
LDLIBS=
OBJECTS= get_bssid

.PHONY: all clean debug
all: $(OBJECTS)
	strip $(OBJECTS)

debug: clean $(OBJECTS) ;

clean:
	rm -f $(OBJECTS)

