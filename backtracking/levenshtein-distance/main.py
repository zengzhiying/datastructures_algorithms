#!/usr/bin/env python3
# coding=utf-8
from levenshtein_distance import Levenshtein

if __name__ == '__main__':
    leven = Levenshtein()

    # 3
    dist1 = leven.distance("mitcmu", "mtacnu")
    print(dist1)

    # 3
    dist2 = leven.distance("kitten", "sitting")
    print(dist2)

    # 192  timeout 调用栈太深
    dist3 = leven.distance("Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine. Write applications quickly in Java, Scala, Python, R, and SQL.",
                           "Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.")
    print(dist3)
