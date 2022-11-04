```
 ********** **             
/////**/// /**             
    /**    /**       ***** 
    /**    /******  **///**
    /**    /**///**/*******
    /**    /**  /**/**//// 
    /**    /**  /**//******
    //     //   //  ////// 
   ******                **           ******   **                   
  **////**              /**          **////** /**                   
 **    //   ******      /**  *****  **    //  /**  ******   ******* 
/**        **////**  ****** **///**/**        /** //////** //**///**
/**       /**   /** **///**/*******/**        /**  *******  /**  /**
//**    **/**   /**/**  /**/**//// //**    ** /** **////**  /**  /**
 //****** //****** //******//****** //******  ***//******** ***  /**
  //////   //////   //////  //////   //////  ///  //////// ///   // 
 **       ** **                                      
/**      // /**                               **   **
/**       **/**      ******  ******   ****** //** ** 
/**      /**/****** //**//* //////** //**//*  //***  
/**      /**/**///** /** /   *******  /** /    /**   
/**      /**/**  /** /**    **////**  /**      **    
/********/**/****** /***   //********/***     **     
//////// // /////   ///     //////// ///     //      
```

# MVP

* ✓ `Book` has title, author, genre.
* ✓ Sample data for mock `Library`.
* Routes:
    1. ✓ list all Books
    2. ✓ show an individual Book
    3. add a new Book to the Library (`POST` route)
    4. ✓ remove a Book from the Library (`POST` route)
* ✓ `base.html` skeleton
* ✓ Styling placeholder with just font

# Extensions

* 'Checked out' _display only_
    * `checked_out` property on Books
    * 'checked out' status on lists and single book pages
* Style everything with CSS
* `POST` route to update `checked_out`

# More extensions?

* Sort the books by title or author
    * eg `/books/sorted/<field>`
    * if the books are sorted, this really messages up using index a book id
* Search or filter?
    * Show books of a specific genre
    * Filter to books not checked out
* Pagination?
* Library should be an object!
* Genre selection should be a drop-down list
* Find out what a 'CSS Reset' would do/be useful for.  Removing annoying margins?
* As you delete books, the book referred to by each index changes!
    * eg /books/1 — delete book 1 — then /books/1 refers to what was /books/2
    * stick a `database_id` attribute on books, `None` by default, and set it
      when added or deleted
* When deleting books, ask 'Are you sure?'
