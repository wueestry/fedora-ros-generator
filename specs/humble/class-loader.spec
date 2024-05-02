# Meta Package
Name:           ros-humble-class-loader
Version:        2.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/class_loader
Summary:        Meta package for ros2-humble-class_loader and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-class_loader
Requires:       ros2-humble-class_loader-devel

Obsoletes: ros-humble-class-loader < 2.2.0-1

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.5.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.2.0-1
- Initial humble build
