# Meta Package
Name:           ros-iron-xacro
Version:        2.0.9
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/xacro
Summary:        Meta package for ros2-iron-xacro and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-xacro
Requires:       ros2-iron-xacro-devel

Obsoletes: ros-iron-xacro < 2.0.9-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.9-1
- Update to latest release
