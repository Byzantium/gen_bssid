#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "extern/md5.h"

#define BSSID_SIZE 6
#define CHAN_SIZE 2

void get_bssid(const char *essid, const unsigned int chan, char *bssid) {
  unsigned char hash[BSSID_SIZE];
  memset(hash, '\0', sizeof(hash));
  char channel[CHAN_SIZE];
  memset(channel, '\0', sizeof(channel));
  int i;
  MD5_CTX ctx;
  MD5_Init(&ctx);

  MD5_Update(&ctx, essid, strlen(essid));
  MD5_Final(hash, &ctx);

  for(i = 0; i < BSSID_SIZE - CHAN_SIZE; i++)
  {
    bssid[i] = hash[i];
  }

  /*
   * Set the first byte to 0x02 (the value of
   * a link-local ethernet address) which is
   * required for a valid bssid.
   */
  bssid[0] = 0x02;

  bssid[i] = chan / 10;
  bssid[i + 1] = chan % 10;

  return;
}

int main (int argc, char** argv) {
	if (argc != 3) {
		printf("Usage: %s <essid> <channel>\n", argv[0]);
		return EXIT_FAILURE;
	}
	char bssid[BSSID_SIZE];
	get_bssid(argv[1], atoi(argv[2]), bssid);
	printf("%s\n", bssid);
	return EXIT_SUCCESS;
}
