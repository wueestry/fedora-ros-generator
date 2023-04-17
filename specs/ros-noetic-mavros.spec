Name:           ros-noetic-mavros
Version:        noetic.1.15.0
Release:        1%{?dist}
Summary:        ROS package mavros

License:        GPLv3
URL:            http://wiki.ros.org/mavros

Source0:        https://github.com/mavlink/mavros-release/archive/release/noetic/mavros/1.15.0-1.tar.gz#/ros-noetic-mavros-1.15.0-source0.tar.gz

Patch0: ros-mavros.build-with-cpp17.patch


# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  gcc
BuildRequires:  GeographicLib
BuildRequires:  GeographicLib-devel
BuildRequires:  gtest-devel
BuildRequires:  libatomic
BuildRequires:  ros-noetic-angles-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-cmake_modules-devel
BuildRequires:  ros-noetic-diagnostic_msgs-devel
BuildRequires:  ros-noetic-diagnostic_updater-devel
BuildRequires:  ros-noetic-eigen_conversions-devel
BuildRequires:  ros-noetic-geographic_msgs-devel
BuildRequires:  ros-noetic-geometry_msgs-devel
BuildRequires:  ros-noetic-libmavconn-devel
BuildRequires:  ros-noetic-mavlink-devel
BuildRequires:  ros-noetic-mavros_msgs-devel
BuildRequires:  ros-noetic-nav_msgs-devel
BuildRequires:  ros-noetic-pluginlib-devel
BuildRequires:  ros-noetic-rosconsole_bridge-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-rosunit-devel
BuildRequires:  ros-noetic-sensor_msgs-devel
BuildRequires:  ros-noetic-std_msgs-devel
BuildRequires:  ros-noetic-std_srvs-devel
BuildRequires:  ros-noetic-tf2_eigen-devel
BuildRequires:  ros-noetic-tf2_ros-devel
BuildRequires:  ros-noetic-trajectory_msgs-devel

Requires:       ros-noetic-diagnostic_msgs
Requires:       ros-noetic-diagnostic_updater
Requires:       ros-noetic-eigen_conversions
Requires:       ros-noetic-geographic_msgs
Requires:       ros-noetic-geometry_msgs
Requires:       ros-noetic-libmavconn
Requires:       ros-noetic-mavros_msgs
Requires:       ros-noetic-message_runtime
Requires:       ros-noetic-nav_msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-rosconsole_bridge
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor_msgs
Requires:       ros-noetic-std_msgs
Requires:       ros-noetic-std_srvs
Requires:       ros-noetic-tf2_eigen
Requires:       ros-noetic-tf2_ros
Requires:       ros-noetic-trajectory_msgs

Provides:  ros-noetic-mavros = 1.15.0-1
Obsoletes: ros-noetic-mavros < 1.15.0-1
Obsoletes: ros-kinetic-mavros < 1.15.0-1



%description
MAVROS -- MAVLink extendable communication node for ROS with proxy for
Ground Control Station.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       eigen3-devel
Requires:       GeographicLib
Requires:       GeographicLib-devel
Requires:       ros-noetic-catkin-devel
Requires:       ros-noetic-mavlink-devel
Requires:       boost-devel
Requires:       gcc
Requires:       gtest-devel
Requires:       libatomic
Requires:       ros-noetic-angles-devel
Requires:       ros-noetic-cmake_modules-devel
Requires:       ros-noetic-diagnostic_msgs-devel
Requires:       ros-noetic-diagnostic_updater-devel
Requires:       ros-noetic-eigen_conversions-devel
Requires:       ros-noetic-geographic_msgs-devel
Requires:       ros-noetic-geometry_msgs-devel
Requires:       ros-noetic-libmavconn-devel
Requires:       ros-noetic-mavros_msgs-devel
Requires:       ros-noetic-nav_msgs-devel
Requires:       ros-noetic-pluginlib-devel
Requires:       ros-noetic-rosconsole_bridge-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-rosunit-devel
Requires:       ros-noetic-sensor_msgs-devel
Requires:       ros-noetic-std_msgs-devel
Requires:       ros-noetic-std_srvs-devel
Requires:       ros-noetic-tf2_eigen-devel
Requires:       ros-noetic-tf2_ros-devel
Requires:       ros-noetic-trajectory_msgs-devel
Requires:       ros-noetic-message_runtime-devel
Requires:       ros-noetic-rospy-devel

Provides: ros-noetic-mavros-devel = 1.15.0-1
Obsoletes: ros-noetic-mavros-devel < 1.15.0-1
Obsoletes: ros-kinetic-mavros-devel < 1.15.0-1


%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}
%patch0 -p1

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
  --pkg mavros




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/mavros/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.15.0-1
- Generate mavlink and mavros
