all: run

run: os.img
	qemu-system-i386 -hda $< -D log.txt -d int -machine smm=off -no-reboot -monitor stdio

os.img:
	make -C loader all
	make -C kern install

clean:
	rm log.txt os.img 2> /dev/null || true
	make -C loader clean
	make -C kern clean

.PHONY: all run clean