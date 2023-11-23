Name:           ros-noetic-rviz
Version:        noetic.1.14.20
Release:        1%{?dist}
Summary:        ROS package rviz

License:        BSD
URL:            http://wiki.ros.org/rviz

Source0:        https://github.com/ros-gbp/rviz-release/archive/release/noetic/rviz/1.14.20-1.tar.gz#/ros-noetic-rviz-1.14.20-source0.tar.gz

Patch0: noetic/rviz.no-rpath.patch
Patch1: noetic/rviz.assimp-decompose-quaternion.patch


# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  assimp
BuildRequires:  assimp-devel
BuildRequires:  eigen3-devel
BuildRequires:  libXext-devel
BuildRequires:  lz4-devel
BuildRequires:  mesa-libGL-devel mesa-libGLU-devel
BuildRequires:  ogre-devel
BuildRequires:  poco-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-sip-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  urdfdom-devel
BuildRequires:  urdfdom-headers-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-cmake_modules-devel
BuildRequires:  ros-noetic-geometry_msgs-devel
BuildRequires:  ros-noetic-image_transport-devel
BuildRequires:  ros-noetic-interactive_markers-devel
BuildRequires:  ros-noetic-laser_geometry-devel
BuildRequires:  ros-noetic-map_msgs-devel
BuildRequires:  ros-noetic-message_filters-devel
BuildRequires:  ros-noetic-message_generation-devel
BuildRequires:  ros-noetic-nav_msgs-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-python_qt_binding-devel
BuildRequires:  ros-noetic-resource_retriever-devel
BuildRequires:  ros-noetic-rosconsole-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-roslib-devel
BuildRequires:  ros-noetic-rospy-devel
BuildRequires:  ros-noetic-rostest-devel
BuildRequires:  ros-noetic-rosunit-devel
BuildRequires:  ros-noetic-sensor_msgs-devel
BuildRequires:  ros-noetic-std_msgs-devel
BuildRequires:  ros-noetic-std_srvs-devel
BuildRequires:  ros-noetic-tf2_geometry_msgs-devel
BuildRequires:  ros-noetic-tf2_ros-devel
BuildRequires:  ros-noetic-urdf-devel
BuildRequires:  ros-noetic-visualization_msgs-devel

Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-noetic-geometry_msgs
Requires:       ros-noetic-image_transport
Requires:       ros-noetic-interactive_markers
Requires:       ros-noetic-laser_geometry
Requires:       ros-noetic-map_msgs
Requires:       ros-noetic-media_export
Requires:       ros-noetic-message_filters
Requires:       ros-noetic-message_runtime
Requires:       ros-noetic-nav_msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-python_qt_binding
Requires:       ros-noetic-resource_retriever
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor_msgs
Requires:       ros-noetic-std_msgs
Requires:       ros-noetic-std_srvs
Requires:       ros-noetic-tf2_geometry_msgs
Requires:       ros-noetic-tf2_ros
Requires:       ros-noetic-urdf
Requires:       ros-noetic-visualization_msgs

Provides:  ros-noetic-rviz = 1.14.20-1
Obsoletes: ros-noetic-rviz < 1.14.20-1
Obsoletes: ros-kinetic-rviz < 1.14.20-1



%description
3D visualization tool for ROS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ogre-devel
Requires:       ros-noetic-catkin-devel
Requires:       assimp
Requires:       assimp-devel
Requires:       eigen3-devel
Requires:       libXext-devel
Requires:       lz4-devel
Requires:       mesa-libGL-devel mesa-libGLU-devel
Requires:       poco-devel
Requires:       python3-qt5-devel
Requires:       python3-sip-devel
Requires:       qt5-qtbase-devel
Requires:       tinyxml2-devel
Requires:       urdfdom-devel
Requires:       urdfdom-headers-devel
Requires:       yaml-cpp-devel
Requires:       ros-noetic-cmake_modules-devel
Requires:       ros-noetic-geometry_msgs-devel
Requires:       ros-noetic-image_transport-devel
Requires:       ros-noetic-interactive_markers-devel
Requires:       ros-noetic-laser_geometry-devel
Requires:       ros-noetic-map_msgs-devel
Requires:       ros-noetic-message_filters-devel
Requires:       ros-noetic-message_generation-devel
Requires:       ros-noetic-nav_msgs-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-python_qt_binding-devel
Requires:       ros-noetic-resource_retriever-devel
Requires:       ros-noetic-rosconsole-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-roslib-devel
Requires:       ros-noetic-rospy-devel
Requires:       ros-noetic-rostest-devel
Requires:       ros-noetic-rosunit-devel
Requires:       ros-noetic-sensor_msgs-devel
Requires:       ros-noetic-std_msgs-devel
Requires:       ros-noetic-std_srvs-devel
Requires:       ros-noetic-tf2_geometry_msgs-devel
Requires:       ros-noetic-tf2_ros-devel
Requires:       ros-noetic-urdf-devel
Requires:       ros-noetic-visualization_msgs-devel
Requires:       ros-noetic-media_export-devel
Requires:       ros-noetic-message_runtime-devel

Provides: ros-noetic-rviz-devel = 1.14.20-1
Obsoletes: ros-noetic-rviz-devel < 1.14.20-1
Obsoletes: ros-kinetic-rviz-devel < 1.14.20-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}
%patch0 -p1
%patch1 -p1

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

PATH="$PATH:%{_qt5_bindir}" ; export PATH
source %{_libdir}/ros/setup.bash

# substitute shebang before install block because we run the local catkin script
%py3_shebang_fix .

DESTDIR=%{buildroot} ; export DESTDIR


catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  -DPYTHON_VERSION=%{python3_version} \
  -DPYTHON_VERSION_NODOTS=%{python3_version_nodots} \
  -DOGRE_PLUGIN_DIR=%{_libdir}/OGRE \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg rviz




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/rviz/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.14.20-1
- Initial desktop generation
