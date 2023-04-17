Name:           ros-noetic-pcl_ros
Version:        noetic.1.7.4
Release:        1%{?dist}
Summary:        ROS package pcl_ros

License:        BSD
URL:            http://ros.org/wiki/perception_pcl

Source0:        https://github.com/ros-gbp/perception_pcl-release/archive/release/noetic/pcl_ros/1.7.4-1.tar.gz#/ros-noetic-pcl_ros-1.7.4-source0.tar.gz

Patch0: ros-pcl_ros.dynamic_reconfigure.patch
Patch1: ros-pcl_ros.build-with-cpp17.patch


# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  eigen3-devel
BuildRequires:  java-17-openjdk-devel
BuildRequires:  libuuid-devel
BuildRequires:  libXext-devel
BuildRequires:  lz4-devel
BuildRequires:  pcl-devel
BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-dynamic_reconfigure-devel
BuildRequires:  ros-noetic-geometry_msgs-devel
BuildRequires:  ros-noetic-message_filters-devel
BuildRequires:  ros-noetic-nodelet-devel
BuildRequires:  ros-noetic-nodelet_topic_tools-devel
BuildRequires:  ros-noetic-pcl_conversions-devel
BuildRequires:  ros-noetic-pcl_msgs-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-rosbag-devel
BuildRequires:  ros-noetic-rosconsole-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-roslib-devel
BuildRequires:  ros-noetic-rostest-devel
BuildRequires:  ros-noetic-sensor_msgs-devel
BuildRequires:  ros-noetic-std_msgs-devel
BuildRequires:  ros-noetic-tf-devel
BuildRequires:  ros-noetic-tf2-devel
BuildRequires:  ros-noetic-tf2_eigen-devel
BuildRequires:  ros-noetic-tf2_ros-devel

Requires:       ros-noetic-dynamic_reconfigure
Requires:       ros-noetic-geometry_msgs
Requires:       ros-noetic-message_filters
Requires:       ros-noetic-nodelet
Requires:       ros-noetic-nodelet_topic_tools
Requires:       ros-noetic-pcl_conversions
Requires:       ros-noetic-pcl_msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor_msgs
Requires:       ros-noetic-std_msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2_eigen
Requires:       ros-noetic-tf2_ros

Provides:  ros-noetic-pcl_ros = 1.7.4-1
Obsoletes: ros-noetic-pcl_ros < 1.7.4-1
Obsoletes: ros-kinetic-pcl_ros < 1.7.4-1



%description
PCL (Point Cloud Library) ROS interface stack. PCL-ROS is the
preferred bridge for 3D applications involving n-D Point Clouds and 3D
geometry processing in ROS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       ros-noetic-dynamic_reconfigure-devel
Requires:       eigen3-devel
Requires:       java-17-openjdk-devel
Requires:       libuuid-devel
Requires:       libXext-devel
Requires:       lz4-devel
Requires:       pcl-devel
Requires:       poco-devel
Requires:       tinyxml-devel
Requires:       tinyxml2-devel
Requires:       ros-noetic-geometry_msgs-devel
Requires:       ros-noetic-message_filters-devel
Requires:       ros-noetic-nodelet-devel
Requires:       ros-noetic-nodelet_topic_tools-devel
Requires:       ros-noetic-pcl_conversions-devel
Requires:       ros-noetic-pcl_msgs-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-rosbag-devel
Requires:       ros-noetic-rosconsole-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-roslib-devel
Requires:       ros-noetic-rostest-devel
Requires:       ros-noetic-sensor_msgs-devel
Requires:       ros-noetic-std_msgs-devel
Requires:       ros-noetic-tf-devel
Requires:       ros-noetic-tf2-devel
Requires:       ros-noetic-tf2_eigen-devel
Requires:       ros-noetic-tf2_ros-devel

Provides: ros-noetic-pcl_ros-devel = 1.7.4-1
Obsoletes: ros-noetic-pcl_ros-devel < 1.7.4-1
Obsoletes: ros-kinetic-pcl_ros-devel < 1.7.4-1


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
  --pkg pcl_ros




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/pcl_ros/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.7.4-1
- Generate desktop-full
