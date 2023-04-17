Name:           ros-noetic-gazebo_ros
Version:        noetic.2.9.2
Release:        1%{?dist}
Summary:        ROS package gazebo_ros

License:        Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros

Source0:        https://github.com/ros-gbp/gazebo_ros_pkgs-release/archive/release/noetic/gazebo_ros/2.9.2-1.tar.gz#/ros-noetic-gazebo_ros-2.9.2-source0.tar.gz

Patch0: ros-gazebo_ros.build-with-cpp17.patch


# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  bullet-devel
BuildRequires:  gazebo-devel
BuildRequires:  libuuid-devel
BuildRequires:  tinyxml-devel
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-cmake_modules-devel
BuildRequires:  ros-noetic-dynamic_reconfigure-devel
BuildRequires:  ros-noetic-gazebo_dev-devel
BuildRequires:  ros-noetic-gazebo_msgs-devel
BuildRequires:  ros-noetic-geometry_msgs-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-rosgraph_msgs-devel
BuildRequires:  ros-noetic-roslib-devel
BuildRequires:  ros-noetic-std_msgs-devel
BuildRequires:  ros-noetic-std_srvs-devel
BuildRequires:  ros-noetic-tf-devel
BuildRequires:  ros-noetic-trajectory_msgs-devel

Requires:       python3
Requires:       ros-noetic-dynamic_reconfigure
Requires:       ros-noetic-gazebo_dev
Requires:       ros-noetic-gazebo_msgs
Requires:       ros-noetic-geometry_msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosgraph_msgs
Requires:       ros-noetic-roslib
Requires:       ros-noetic-std_msgs
Requires:       ros-noetic-std_srvs
Requires:       ros-noetic-tf

Provides:  ros-noetic-gazebo_ros = 2.9.2-1
Obsoletes: ros-noetic-gazebo_ros < 2.9.2-1
Obsoletes: ros-kinetic-gazebo_ros < 2.9.2-1



%description
Provides ROS plugins that offer message and service publishers for
interfacing with

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       bullet-devel
Requires:       gazebo-devel
Requires:       libuuid-devel
Requires:       tinyxml-devel
Requires:       ros-noetic-cmake_modules-devel
Requires:       ros-noetic-dynamic_reconfigure-devel
Requires:       ros-noetic-gazebo_dev-devel
Requires:       ros-noetic-gazebo_msgs-devel
Requires:       ros-noetic-geometry_msgs-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-rosgraph_msgs-devel
Requires:       ros-noetic-roslib-devel
Requires:       ros-noetic-std_msgs-devel
Requires:       ros-noetic-std_srvs-devel
Requires:       ros-noetic-tf-devel
Requires:       ros-noetic-trajectory_msgs-devel

Provides: ros-noetic-gazebo_ros-devel = 2.9.2-1
Obsoletes: ros-noetic-gazebo_ros-devel < 2.9.2-1
Obsoletes: ros-kinetic-gazebo_ros-devel < 2.9.2-1


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
  --pkg gazebo_ros




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/gazebo_ros/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.2.9.2-1
- Generate desktop-full
