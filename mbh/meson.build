#######################################################################
# Internal includes

inc_dir = 'include'

inc_mbh = include_directories( inc_dir )

#######################################################################
# MBH Lib

mbh_lib = library( 'mbh',
                   [ 'src/mbh.cpp' ],
       	 	   include_directories : [ inc_mbh ],
		   dependencies : [ ],
                   install : true )

mbh_dep = declare_dependency( link_with : mbh_lib,
                              include_directories : [ inc_mbh ] )

lib_headers += [ root + '/mbh/' + inc_dir + '/mbh.h' ]

#######################################################################
# MBH Lib C Interface

#######################################################################
