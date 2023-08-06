#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>

void open_directory(char* dir);
int open_directory_helper(char* dir, int* dir_counter_p, int* file_counter_p, unsigned long* byte_counter_p, int depth);
int show_hidden = 0; //default false
int show_bytes = 0; // default false

int main(int argc, char *argv[]) {
	int argi = 1; //index, don't care about 0
		      //
	while (argi < argc && (strcmp(argv[argi], "-a") == 0 || strcmp(argv[argi], "-s") ==0 )) {
		if (strcmp(argv[argi], "-a") == 0) {
			show_hidden = 1;
		} else {
			show_bytes = 1;
		}
		argi++;
	}

	if (argi == argc) {
		open_directory(".");
	} else { //there is a swtich
		while (argi < argc) {
			open_directory(argv[argi]);
			argi++;
		}
	}
}

	// recursively print contents of directory:
	// base: directory has nothing in it
	// depth first search

void open_directory(char* dir) {
	int dir_counter = 0;
	int file_counter = 0;
	unsigned long byte_counter = 0;
	printf("%s\n", dir);

	int result = open_directory_helper(dir, &dir_counter, &file_counter, &byte_counter, 1);
	if (result) { // if its not 0
		return;
	}

	struct stat statbuf;
		
	if (show_bytes) { // true if non zero
		lstat(dir, &statbuf);
		byte_counter += statbuf.st_size;
	}
	
	if (show_bytes) {
		printf("%12lu  bytes used in ", byte_counter);
	}
	printf("%d directories, %d files\n", dir_counter, file_counter);
}

int compare(const void* p1, const void* p2) {
	struct dirent *d1  = (struct dirent *)p1;
	struct dirent *d2 = (struct dirent *)p2;
	return strcmp(d1->d_name, d2->d_name);
}

int open_directory_helper(char* dir, int* dir_counter_p, int* file_counter_p, unsigned long* byte_counter_p, int depth) {
	
	//char cwd[4096];
	//getcwd(cwd, 4096);

	char* cwd = getcwd(NULL, 0); //this is gonna be malloced and i have to free it
	int result = chdir(dir); // cd'ing into dir
	if (result != 0) {
		printf("This is not a directory.\n");
		free(cwd);
		return -1;
	}

	DIR* dir_stream = opendir(".");
	struct dirent* dir_entry = readdir(dir_stream); // pointer to a struct that has info about dir
	
	int counter = 0;

	
	while (dir_entry != NULL) {
		if (strcmp(dir_entry->d_name, ".") == 0 || strcmp(dir_entry->d_name, "..") == 0) {
			dir_entry = readdir(dir_stream);
			continue;
		}
		counter++;

		dir_entry = readdir(dir_stream);
	}
	closedir(dir_stream);
	
	struct dirent file_info[counter];
	dir_stream = opendir(".");
	for (int i = 0; i < counter; i++) {
		dir_entry = readdir(dir_stream);
		if (strcmp(dir_entry->d_name, ".") == 0 || strcmp(dir_entry->d_name, "..") == 0) {
			i--;
			continue;
		}
		file_info[i] = *dir_entry;
	}
	
	closedir(dir_stream); //dir stream is the pointer to the book and dir entry is a page in the book
	
	// alphabetical sort
	qsort(file_info, counter, sizeof(struct dirent), compare);

	struct stat statbuf;
	  
	for (int j = 0; j < counter; j++) {
		if (file_info[j].d_name[0] == '.' && show_hidden == 0) {
			continue;
		}
		

		for (int k = 0; k < depth; k++) {
			if (k != (depth - 1)) { // checks if last in thr row 
				printf("|   ");
			} else if (j == (counter - 1)) { // if last entry in current folder 
				printf("`-- ");
			} else {
				printf("|-- ");
			}
		}
		
		if (show_bytes) { // true if non zero
			lstat(file_info[j].d_name, &statbuf);
			(*byte_counter_p) += statbuf.st_size;
			printf("[%11lu]  ", statbuf.st_size);
		}

		// printf("%d:", depth);
		printf("%s\n", file_info[j].d_name);
		

		if (file_info[j].d_type == DT_DIR) {
			(*dir_counter_p)++;
			open_directory_helper(file_info[j].d_name, dir_counter_p, file_counter_p, byte_counter_p, depth+1);
		} else {
			(*file_counter_p)++;
		}

	}


	chdir(cwd);
	free(cwd);
	return 0;
}


