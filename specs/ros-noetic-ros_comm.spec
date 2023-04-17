Name:           ros-noetic-ros_comm
Version:        noetic.1.16.0
Release:        1%{?dist}
Summary:        ROS package ros_comm

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/ros_comm-release/archive/release/noetic/ros_comm/1.16.0-1.tar.gz#/ros-noetic-ros_comm-1.16.0-source0.tar.gz


BuildArch: noarch

# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  ros-noetic-catkin-devel

Requires:       ros-noetic-message_filters
Requires:       ros-noetic-ros
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosgraph
Requires:       ros-noetic-rosgraph_msgs
Requires:       ros-noetic-roslaunch
Requires:       ros-noetic-roslisp
Requires:       ros-noetic-rosmaster
Requires:       ros-noetic-rosmsg
Requires:       ros-noetic-rosnode
Requires:       ros-noetic-rosout
Requires:       ros-noetic-rosparam
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rosservice
Requires:       ros-noetic-rostest
Requires:       ros-noetic-rostopic
Requires:       ros-noetic-roswtf
Requires:       ros-noetic-std_srvs
Requires:       ros-noetic-topic_tools
Requires:       ros-noetic-xmlrpcpp

Provides:  ros-noetic-ros_comm = 1.16.0-1
Obsoletes: ros-noetic-ros_comm < 1.16.0-1
Obsoletes: ros-kinetic-ros_comm < 1.16.0-1



%description
ROS communications-related packages, including core client libraries
(roscpp, rospy) and graph introspection tools (rostopic, rosnode,
rosservice, rosparam).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       ros-noetic-message_filters-devel
Requires:       ros-noetic-ros-devel
Requires:       ros-noetic-rosbag-devel
Requires:       ros-noetic-rosconsole-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-rosgraph-devel
Requires:       ros-noetic-rosgraph_msgs-devel
Requires:       ros-noetic-roslaunch-devel
Requires:       ros-noetic-roslisp-devel
Requires:       ros-noetic-rosmaster-devel
Requires:       ros-noetic-rosmsg-devel
Requires:       ros-noetic-rosnode-devel
Requires:       ros-noetic-rosout-devel
Requires:       ros-noetic-rosparam-devel
Requires:       ros-noetic-rospy-devel
Requires:       ros-noetic-rosservice-devel
Requires:       ros-noetic-rostest-devel
Requires:       ros-noetic-rostopic-devel
Requires:       ros-noetic-roswtf-devel
Requires:       ros-noetic-std_srvs-devel
Requires:       ros-noetic-topic_tools-devel
Requires:       ros-noetic-xmlrpcpp-devel

Provides: ros-noetic-ros_comm-devel = 1.16.0-1
Obsoletes: ros-noetic-ros_comm-devel < 1.16.0-1
Obsoletes: ros-kinetic-ros_comm-devel < 1.16.0-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

DESTDIR=%{buildroot} ; export DESTDIR


catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  -DPYTHON_VERSION=%{python3_version} \
  -DPYTHON_VERSION_NODOTS=%{python3_version_nodots} \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg ros_comm




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/ros_comm/cmake} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list



# replace cmake python macro in shebang
for file in $(grep -rIl '^#!.*@PYTHON_EXECUTABLE@.*$' %{buildroot}) ; do
  sed -i.orig 's:^#!\s*@PYTHON_EXECUTABLE@\s*:%{__python3}:' $file
  touch -r $file.orig $file
  rm $file.orig
done


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See https://pagure.io/ros for more information." >> README_FEDORA
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -m 0644 -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list

%py3_shebang_fix %{buildroot}

# Also fix .py.in files
for pyfile in $(grep -rIl '^#!.*python.*$' %{buildroot}) ; do
  %py3_shebang_fix $pyfile
done


%files -f files.list
%files devel -f files_devel.list


%changelog
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.16.0-1
- Initial desktop generation
