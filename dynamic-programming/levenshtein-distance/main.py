#!/usr/bin/env python3
# coding=utf-8
from levenshtein_distance import distance

if __name__ == '__main__':
    # 3
    print(distance("mitcmu", "mtacnu"))

    # 3
    print(distance("kitten", "sitting"))

    # 192
    dist = distance("Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine. Write applications quickly in Java, Scala, Python, R, and SQL.",
                    "Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.")

    print(dist)
