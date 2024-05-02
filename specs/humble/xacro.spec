# Meta Package
Name:           ros-humble-xacro
Version:        2.0.8
Release:        2%{?dist}
License:        BSD
URL:            http://ros.org/wiki/xacro
Summary:        Meta package for ros2-humble-xacro and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-xacro
Requires:       ros2-humble-xacro-devel

Obsoletes: ros-humble-xacro < 2.0.8-2

%description
Xacro (XML Macros) Xacro is an XML macro language. With xacro, you can
construct shorter and more readable XML files by using macros that
expand to larger XML expressions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Mar 21 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.8-2
- fix regex warning
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.8-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.8-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.8-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.14.15-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.8-1
- Initial humble build
