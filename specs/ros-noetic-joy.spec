Name:           ros-noetic-joy
Version:        noetic.1.15.1
Release:        1%{?dist}
Summary:        ROS package joy

License:        BSD
URL:            http://www.ros.org/wiki/joy

Source0:        https://github.com/ros-gbp/joystick_drivers-release/archive/release/noetic/joy/1.15.1-1.tar.gz#/ros-noetic-joy-1.15.1-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command

BuildRequires:  linuxconsoletools
BuildRequires:  ros-noetic-catkin-devel
BuildRequires:  ros-noetic-diagnostic_updater-devel
BuildRequires:  ros-noetic-rosbag-devel
BuildRequires:  ros-noetic-roscpp-devel
BuildRequires:  ros-noetic-roslint-devel
BuildRequires:  ros-noetic-sensor_msgs-devel

Requires:       linuxconsoletools
Requires:       ros-noetic-diagnostic_updater
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor_msgs

Provides:  ros-noetic-joy = 1.15.1-1
Obsoletes: ros-noetic-joy < 1.15.1-1
Obsoletes: ros-kinetic-joy < 1.15.1-1



%description
ROS driver for a generic Linux joystick. The joy package contains
joy_node, a node that interfaces a generic Linux joystick to ROS. This
node publishes a "Joy" message, which contains the current state of
each one of the joystick's buttons and axes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-noetic-catkin-devel
Requires:       linuxconsoletools
Requires:       ros-noetic-diagnostic_updater-devel
Requires:       ros-noetic-rosbag-devel
Requires:       ros-noetic-roscpp-devel
Requires:       ros-noetic-roslint-devel
Requires:       ros-noetic-sensor_msgs-devel

Provides: ros-noetic-joy-devel = 1.15.1-1
Obsoletes: ros-noetic-joy-devel < 1.15.1-1
Obsoletes: ros-kinetic-joy-devel < 1.15.1-1


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
  --pkg joy




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,local_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig,share/joy/cmake} \
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
* 2023-04-17 Ryan Wüest <ryan.wueest@protonmail.com> - noetic.1.15.1-1
- Generate joy and ackermann_msgs packages
