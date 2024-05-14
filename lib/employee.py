from __init__ import CURSOR
from review import Review  # Embedding import to avoid circular import issues

class Employee:

    # Existing class methods and properties omitted for brevity...

    def reviews(self):
        """Return list of reviews associated with current employee"""
        # Embedding import to avoid circular import issues
        from review import Review  

        # Query the "reviews" table to get all rows where the foreign key column employee_id matches the id of the current Employee instance
        sql = """
            SELECT * FROM reviews WHERE employee_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()

        # Return a list of Review instances for each matching table row
        return [Review.instance_from_db(row) for row in rows]
