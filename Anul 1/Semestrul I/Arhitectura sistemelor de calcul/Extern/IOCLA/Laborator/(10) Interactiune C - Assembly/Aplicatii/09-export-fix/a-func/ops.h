/* SPDX-License-Identifier: BSD-3-Clause */

#ifndef OPS_H_
#define OPS_H_		1

void init(void);
void set(int value);
int get(void);

extern int age;
void print_age(void);

#endif
