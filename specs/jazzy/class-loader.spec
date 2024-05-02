# Meta Package
Name:           ros-jazzy-class-loader
Version:        2.7.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/class_loader
Summary:        Meta package for ros2-jazzy-class_loader and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-class_loader
Requires:       ros2-jazzy-class_loader-devel

Obsoletes: ros-jazzy-class-loader < 2.7.0-1

%description
The class_loader package is a ROS-independent package for loading
plugins during runtime and the foundation of the higher level ROS
"pluginlib" library. class_loader utilizes the host operating system's
runtime loader to open runtime libraries (e.g. .so/.dll files),
introspect the library for exported plugin classes, and allows users
to instantiate objects of these exported classes without the explicit
declaration (i.e. header file) for those classes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.7.0-1
- Update to latest release
