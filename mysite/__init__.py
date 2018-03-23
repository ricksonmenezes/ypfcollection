#!/usr/bin/env python
+try:
+    import pymysql
+    pymysql.install_as_MySQLdb()
+except ImportError:
+    pass